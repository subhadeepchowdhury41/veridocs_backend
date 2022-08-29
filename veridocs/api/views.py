from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from django.core import exceptions
from .serializers import FormSerializer
from .models import Form

# Create your views here.

@api_view(['GET'])
def getAllForms(request):
    forms = Form.objects.all()
    serializer = FormSerializer(forms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getForm(request, pk):
    form = Form.objects.get(id=pk)
    serializer = FormSerializer(form, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addForm(request):
    serializer = FormSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteForm(request, pk):
    try:
        form = Form.objects.get(id=pk)
        form.delete()
        return Response({"result": "Deleted Successfully"})
    except exceptions.ObjectDoesNotExist:
        return Response({"result": "No forms with given ID",}, status=505)

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