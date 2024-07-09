
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('setestcookie/',views.settestcookie),
    path('setsession/',views.setsession,name='home'),
    path('getsession/',views.getsession,name='getsession'),
    path('delsession/',views.delSession,name="delsession")
]