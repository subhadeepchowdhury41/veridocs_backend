from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from django.core import exceptions
from .serializers import FormSerializer, TemplateSerializer
from .models import Form, Template

# Create your views here.

@api_view(['GET'])
def getAllForms(request):
    forms = Form.objects.all()
    serializer = FormSerializer(forms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getForm(request, pk):
    try:
        form = Form.objects.get(id=pk)
        serializer = FormSerializer(form, many=False)
        return Response(serializer.data)
    except exceptions.ObjectDoesNotExist:
        return Response({"result": "No forms with given ID",}, status=404)

@api_view(['POST'])
def addForm(request):
    serializer = FormSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({"result": "Not valid data", "data": serializer.data}, status=404)

@api_view(['DELETE'])
def deleteForm(request, pk):
    try:
        form = Form.objects.get(id=pk)
        form.delete()
        return Response({"result": "Deleted Successfully"})
    except exceptions.ObjectDoesNotExist:
        return Response({"result": "No forms with given ID",}, status=404)

@api_view(['PUT'])
def updateData(request, pk):
    try:
        form = Form.objects.get(id=pk)
        serializer = FormSerializer(form, data=request.data)
        if not serializer.is_valid():
            print("...")
            return Response(serializer.errors, status=404)
        else:
            serializer.save()
            return Response(serializer.data, status=200)
    except exceptions.ObjectDoesNotExist:
        return Response({"result": "No Form with given ID"})
    except exceptions.BadRequest:
        return Response({"result": "Page not found"})


@api_view(['GET'])
def getAllTemplates(request):
    templates = Template.objects.all()
    serializer = FormSerializer(templates, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTemplatesByCompany(request, pk):
    templates = Template.objects.all().filter(agency=pk)
    serializer = TemplateSerializer(templates, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTemplate(request, pk):
    try:
        template = Template.objects.get(id=pk)
        serializer = TemplateSerializer(template, many=False)
        return Response(serializer.data)
    except exceptions.ObjectDoesNotExist:
        return Response({"result": "No Temaplates with given ID",}, status=404)

@api_view(['POST'])
def addTemplate(request):
    serializer = TemplateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({"result": "Not valid data", "data": serializer.data}, status=404)

@api_view(['DELETE'])
def deleteTemplate(request, pk):
    try:
        template = Template.objects.get(id=pk)
        template.delete()
        return Response({"result": "Deleted Successfully"})
    except exceptions.ObjectDoesNotExist:
        return Response({"result": "No Templates with given ID",}, status=404)

@api_view(['PUT'])
def updateTemplateData(request, pk):
    try:
        template = Template.objects.get(id=pk)
        serializer = TemplateSerializer(template, data=request.data)
        if not serializer.is_valid():
            print("...")
            return Response(serializer.errors, status=404)
        else:
            serializer.save()
            return Response(serializer.data, status=200)
    except exceptions.ObjectDoesNotExist:
        return Response({"result": "No Form with given ID"})
    except exceptions.BadRequest:
        return Response({"result": "Page not found"})
