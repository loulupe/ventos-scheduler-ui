from django.db import models

# Create your models here.
class BuildingDoc(models.Model):
    name = models.CharField(max_length = 80)
    docfile = models.FileField(upload_to='buildingDocs/%Y/%m/%d')
    def __str__(self):
        return self.name

class RegDoc(models.Model):
    name = models.CharField(max_length = 80)
    docfile = models.FileField(upload_to='registrationDocs/%Y/%m/%d')
    buildfile = models.ForeignKey('BuildingDoc',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name



class Registration(models.Model):
    term = models.IntegerField()
    session = models.IntegerField()
    acadGroup = models.CharField(max_length = 10)
    subject = models.CharField(max_length = 10)
    catalog = models.CharField(max_length = 20)
    sectionComponent = models.CharField(max_length = 255)
    descr = models.CharField(max_length = 255)
    classNbr = models.IntegerField()
    campus = models.CharField(max_length = 255)
    totEnrl = models.IntegerField()
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    facilID = models.CharField(max_length = 255)
    mtgStart = models.DateTimeField()
    mtgEnd = models.DateTimeField()
    mon = models.CharField(max_length = 1)
    tues = models.CharField(max_length = 1)
    wed = models.CharField(max_length = 1)
    thurs = models.CharField(max_length = 1)
    fri = models.CharField(max_length = 1)
    sat = models.CharField(max_length = 1)
    sun = models.CharField(max_length = 1)
    startDate  = models.DateTimeField()
    endDate = models.DateTimeField()
    relatedBuild = models.IntegerField()
    status = models.IntegerField()
    
    
class buildingdata(models.Model):
    building = models.CharField(max_length = 70)
    room = models.BigIntegerField()
    facilityId = models.CharField(max_length = 70)
    capacity = models.PositiveIntegerField()
    typeRoom = models.CharField(max_length = 70)
    acadOrg = models.CharField(max_length = 20)
    area = models.PositiveIntegerField()
    maxOccupant = models.PositiveIntegerField()
    roomName = models.CharField(max_length = 70)
    spaceCategory = models.CharField(max_length = 70)
    system = models.CharField(max_length= 10)
    vav = models.CharField(max_length = 20)
    indUnit = models.CharField(max_length = 30)
    idleAirflow = models.IntegerField()
    activeAirflow = models.IntegerField()
    builddoc = models.ForeignKey('BuildingDoc',on_delete=models.CASCADE)


class airflow(models.Model):
    facilID = models.CharField(max_length = 70)
    typeOfFacility = models.CharField(max_length = 70)
    system = models.CharField(max_length = 70)
    vav = models.CharField(max_length = 70)
    areaSqft = models.DecimalField(max_digits=11,decimal_places=2)
    occupants = models.DecimalField(max_digits=11,decimal_places=2)
    raOutAirRateArea = models.DecimalField(max_digits=11,decimal_places=2)
    raOutAirRatePerson = models.DecimalField(max_digits=11,decimal_places=2)
    vbz = models.DecimalField(max_digits=11,decimal_places=2)
    ez = models.DecimalField(max_digits=11,decimal_places=2)
    voz = models.DecimalField(max_digits=11,decimal_places=2)
    ev = models.DecimalField(max_digits=11,decimal_places=2)
    vot = models.DecimalField(max_digits=11,decimal_places=2)
    leed = models.DecimalField(max_digits=11,decimal_places=2)
    leedVot = models.DecimalField(max_digits=11,decimal_places=2)
    occupiedMaxAirflow = models.DecimalField(max_digits=11,decimal_places=2)
    occupiedReqAirflow = models.DecimalField(max_digits=11,decimal_places=2)
    reqDamperPosition = models.DecimalField(max_digits=11,decimal_places=2)
    occupiedIdleAirflow = models.DecimalField(max_digits=11,decimal_places=2)
    idleDamperPosition = models.DecimalField(max_digits=11,decimal_places=2)
    status = models.IntegerField()

class VentRate(models.Model):
    spaceCategory = models.CharField(max_length = 70)
    airRatePerson = models.DecimalField(max_digits=5,decimal_places=2)
    airRateArea = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return str(self.spaceCategory +'||'+ str(self.airRatePerson) +'||'+ str(self.airRateArea))

class AirDistConf(models.Model):
    configuration = models.CharField(max_length = 255)
    value = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return str(self.configuration)

class SysVentEfficiency(models.Model):
    ZpMax = models.DecimalField(max_digits=5,decimal_places=2)
    Ev = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return str(self.Ev)

