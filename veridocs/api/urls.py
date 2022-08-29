from django.urls import path
from . import views

urlpatterns = [
    path('forms', views.getAllForms, name='get-all-forms'),
    path('form/create', views.addForm, name='add-form'),
    path('form/<str:pk>', views.getForm, name='get-form-info'),
    path('form/update/<str:pk>', views.updateData, name='upadte-form'),
    path('form/delete/<str:pk>', views.deleteForm, name='delete-form'),
    
]
