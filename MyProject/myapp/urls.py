from django.urls import path
from myapp import views


urlpatterns = [
    path('',views.home,name='home'),
    path('form/',views.form,name='form'),
    path('display/',views.display,name='display')

]
