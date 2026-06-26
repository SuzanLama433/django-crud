from django.urls import path
from .views import *

urlpatterns = [
  path('' ,home, name='home'),
  path('form/',form,name='form'),
  path('result/',show,name='show'),
  path('about/',about,name='about'),
  path('contact/',contact,name='contact'),
  path('delete/<int:id>',delete_data,name='delete'),
  path('edit/<int:id>',edit,name='edit'),
  path('restore/',restoreItem,name='restore'),
  path('restoreItem/<int:id>',restore_data,name='restoreItem'),
  path('strongDelete/<int:id>',delete_permanent,name='strongDelete'),
  path('deleteAll/',delete_all,name='deleteAll')
]