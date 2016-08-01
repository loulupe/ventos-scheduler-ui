from django.conf.urls import url

from scheduler import views
app_name = 'scheduler'
urlpatterns = [
            url(r'^add/$', views.add,name='add' ),
            url(r'^addreg/$', views.addreg,name='addreg' ),
            url(r'^schedule_reg/$',views.schedule_reg,name='schedule_reg'),
            url(r'^scheduledetail/(?P<buildid>\d+)$',views.scheduledetail,name='scheduledetail')

            ]
