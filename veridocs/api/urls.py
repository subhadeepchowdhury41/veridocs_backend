from django.urls import path
from . import views

urlpatterns = [
    path('forms', views.getAllForms, name='get-all-forms'),
    path('form/create', views.addForm, name='add-form'),
    path('form/<str:pk>', views.getForm, name='get-form-info'),
    path('form/update/<str:pk>', views.updateData, name='upadte-form'),
    path('form/delete/<str:pk>', views.deleteForm, name='delete-form'),
    path('templates', views.getAllTemplates, name='get-all-templates'),
    path('templates/<str:pk>', views.getTemplatesByCompany, name='get-templates-by-compoany'),
    path('template/create', views.addTemplate, name='add-template'),
    path('template/update/<str:pk>', views.updateTemplateData, name='update-template'),
    path('template/delete/<str:pk>', views.deleteTemplate, name='delete-template'),
    path('template/<str:pk>', views.getTemplate, name='get-template')
]
