from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from scheduler.forms import BuildingDataForm,RegistrationDataForm,RegisterScheduleForm,airflowform
from scheduler.models import RegDoc,BuildingDoc,buildingdata,Registration,airflow,VentRate,SysVentEfficiency,AirDistConf
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
import csv
import os
from scheduler.utils import read_and_filter_csv,is_whitespace
import dateutil.parser
from django.forms import formset_factory
import decimal
# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def index(request):
    return HttpResponse('Grid for the scheduler show here')

def schedule_reg(request):
    if request.method == 'POST':
        form = RegisterScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            registerDoc = RegDoc.objects.get(id = str(form.cleaned_data['registerchoices'].id))
            if registerDoc:
                return HttpResponseRedirect(reverse('scheduler:scheduledetail',kwargs={'buildid':str(registerDoc.buildfile.id)}))
            else:
                return HttpResponse("No registration document was found")
    else:
        form = RegisterScheduleForm()
    return render_to_response('scheduler/schedule_reg.html',{'form': form},context_instance=RequestContext(request))

def scheduledetail(request,buildid):
    AirflowFormSet = formset_factory(airflowform,extra=0)
    if request.method == 'POST':
        formset = AirflowFormSet(request.POST)
        print('Step 1')
        if formset.is_valid():
            print('validated')
            for form in formset:
                identifier = form.cleaned_data['regid']
                r_item = Registration.objects.get(id = identifier)
                EvId = form.cleaned_data['EvChoice'].Ev
                EzId = form.cleaned_data['EzChoice'].value
                print("EZ value:"+str(EzId))
                schedule(r_item,buildid,EzId,EvId)
            return render_to_response('ventos/home.html')
        else:
            return render_to_response('scheduler/scheduledetail.html',{'formset': formset,'buildid':buildid},context_instance=RequestContext(request))

    else:
        entries = list()
        print("BUILD"+str(buildid))
        all_reg = Registration.objects.filter(relatedBuild = buildid).all()
        for r_item in all_reg:
           vent = VentRate.objects.all()[0]
           conf = AirDistConf.objects.all()[0]
           eff = SysVentEfficiency.objects.all()[0]
           initial = {
                'regid':r_item.pk,
                'facility':r_item.facilID,
                'enrollment':r_item.totEnrl,
                'space':r_item.sectionComponent,
                'starttime':str((r_item.mtgStart).time()),
                'endtime':str((r_item.mtgEnd).time()),
                'EzChoice':conf,
                'EvChoice':eff
                }
           entries.append(initial)
        formset = AirflowFormSet(initial=entries)
        return render_to_response('scheduler/scheduledetail.html',{'formset': formset,'buildid':buildid},context_instance=RequestContext(request))

        
def schedule(r_item,buildid,Ez,Ev):
    b_data = buildingdata.objects.filter(builddoc_id = buildid).all()
    AirRateP = 1
    AirRateA = 1
    print("Reg"+str(r_item.facilID) + "BUILD" +str(buildid))
    for bitem in b_data:
        print("Building"+bitem.facilityId)
        if (r_item.facilID  == bitem.facilityId):
            print('Found Match')
            vents = VentRate.objects.filter(spaceCategory = bitem.spaceCategory).all()
            for v in vents:
                print('Found Vent')
                AirRateP = v.airRatePerson
                AirRateA = v.airRateArea
                break
            createAirflow(r_item,bitem,AirRateA,AirRateP,Ez,Ev)
            break

def createAirflow(ritem,bitem,airRateArea,airRatePerson,Ez,Ev):
    print("AirRateArea"+str(airRateArea))
    print("AirRatePerson"+str(airRatePerson))
    print("Ez:"+str(Ez))
    print("Ev:"+str(Ev))
    print("Area"+str(bitem.area))
    vbz_calc = (airRatePerson * (ritem.totEnrl + 1)) + (airRateArea * bitem.area)
    Voz = vbz_calc * Ez
    Vot = Voz * Ev
    leed = decimal.Decimal(1.3)
    leedvot = leed * Vot
    if (leedvot > bitem.idleAirflow):
        req = leedvot
    else:
        req = bitem.idleAirflow
    print("Req"+str(req))
    print("ACtive"+str(bitem.activeAirflow))
    print("Idle airflow"+str(bitem.idleAirflow))
    damper = (req/bitem.activeAirflow) * 100
    idle =  (bitem.idleAirflow/bitem.activeAirflow) * 100
    air_object = airflow(
            facilID = ritem.facilID,
            typeOfFacility = bitem.spaceCategory,
            system = bitem.system,
            vav = bitem.vav,
            areaSqft = bitem.area,
            occupants = int(ritem.totEnrl + 1),
            raOutAirRateArea = airRateArea,
            raOutAirRatePerson = airRatePerson,
            vbz = vbz_calc,
            ez = Ez,
            voz = Voz,
            ev = Ev,
            vot = Vot,
            leed = leed,
            leedVot = leedvot,
            occupiedMaxAirflow = bitem.activeAirflow,
            occupiedIdleAirflow = bitem.idleAirflow,
            occupiedReqAirflow = req,
            reqDamperPosition = damper,
            idleDamperPosition = idle,
            status = '1'
            )
    air_object.save()
    
def add(request):
    if request.method == 'POST':
        form = BuildingDataForm(request.POST, request.FILES)
        if form.is_valid():
            print('Form was valid')
            newdoc = BuildingDoc(
                    name = form.cleaned_data['name'],
                    docfile = request.FILES['docfile'],
                    )
            newdoc.save()
            path = newdoc.docfile.url
            uploadBuilding(os.path.join(BASE_DIR,path),newdoc)
            # Redirect to the document list after POST
            return render_to_response('ventos/home.html')
        else:
            documents = RegDoc.objects.all()
        # Render list page with the documents and the form
        return render_to_response('scheduler/buildlist.html',{'documents': documents, 'form': form},context_instance=RequestContext(request))
    else:
        form = BuildingDataForm() # A empty, unbound form
        # Load documents for the list page
        documents = RegDoc.objects.all()
        # Render list page with the documents and the form
        return render_to_response('scheduler/buildlist.html',{'documents': documents, 'form': form},context_instance=RequestContext(request))

def addreg(request):
    if request.method == 'POST':
        form = RegistrationDataForm(request.POST, request.FILES)
        if form.is_valid():
            builddoc = BuildingDoc.objects.get(id = form.cleaned_data['buildingchoices'].id)
            newdoc = RegDoc(name = form.cleaned_data['name'],docfile = request.FILES['regdocfile'],buildfile=builddoc)
            newdoc.save(force_insert = True)
            path = newdoc.docfile.url
            uploadRegistration(os.path.join(BASE_DIR,path),builddoc)
            return render_to_response('ventos/home.html')
        else:
            documents = BuildingDoc.objects.all()
            return render_to_response('scheduler/reglist.html',{'documents': documents, 'form': form},context_instance=RequestContext(request))
    else:
        form = RegistrationDataForm()
        documents = BuildingDoc.objects.all()
        return render_to_response('scheduler/reglist.html',{'documents': documents, 'form': form},context_instance=RequestContext(request))

def uploadRegistration(path,doc):
    buildid = doc.id
    with open(path) as fileName:
        non_blank = (line for line in fileName if line.strip())
        has_header = csv.Sniffer().has_header(fileName.read(1024))
        fileName.seek(0)  # rewind
        reader = csv.reader(fileName)
        if has_header:
            next(reader) 
        for row in reader:
            if any(field.strip() for field in row):
                _,created = Registration.objects.get_or_create(
                        term = row[0],
                        session = row[1],
                        acadGroup = row[2],
                        subject = row[3],
                        catalog = row[4],
                        sectionComponent = row[6],
                        descr = row[7],
                        classNbr = row[8],
                        campus = row[9],
                        totEnrl = int(row[10] or 0),
                        startDate = dateutil.parser.parse(row[11]),
                        endDate = dateutil.parser.parse(row[12]),
                        facilID = row[16],
                        mtgStart = dateutil.parser.parse(row[17]),
                        mtgEnd = dateutil.parser.parse(row[18]),
                        mon = row[19],
                        tues = row[20],
                        wed =  row[21],
                        thurs = row[22],
                        fri = row[23],
                        sat = row[24],
                        sun = row[25],
                        relatedBuild = buildid,
                        status = '1'
                        )

def uploadBuilding(path,doc):
    print('##############################Enter################')
    with open(path) as fileName:
        non_blank = (line for line in fileName if line.strip())
        has_header = csv.Sniffer().has_header(fileName.read(1024))
        fileName.seek(0)  # rewind
        reader = csv.reader(fileName)
        if has_header:
            next(reader) 
        for row in reader:
            if any(field.strip() for field in row):
                _, created = buildingdata.objects.get_or_create(
                        building = row[0],
                        room = int(row[1] or 0),
                        facilityId = row[2],
                        capacity = int(row[3] or 0),
                        typeRoom = row[4],
                        acadOrg = row[5],
                        area = int(row[9] or 0),
                        maxOccupant = int(row[10] or 0),
                        roomName = row[11],
                        spaceCategory = row[12],
                        system = row[13],
                        vav = row[14],
                        indUnit = row[15],
                        idleAirflow = int (row[17] or 0),
                        activeAirflow = int (row[18] or 0),
                        builddoc = doc
                        )
