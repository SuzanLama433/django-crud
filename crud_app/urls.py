from django.urls import path
from .views import *

urlpatterns = [
  path('' ,home, name='home'),
  path('form/',form,name='form'),
  path('result/',show,name='show'),
  path('about/',about,name='about'),
  path('contact/',contact,name='contact'),
  path('delete/<int:id>',delete_data,name='delete'),
  path('edit/<int:id>',edit,name='edit')
]