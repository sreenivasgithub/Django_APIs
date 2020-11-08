from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import StudentModel
from .serializers import StudentSerializer

# Create your views here.

@api_view(['GET'])
def studentView(request):
    task = StudentModel.objects.all()
    serializer = StudentSerializer(task, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def singleStudentView(request, pk):
    task = StudentModel.objects.get(id=pk)
    serializer = StudentSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def studentPostView(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def studentUpdateView(request, pk):
    task = StudentModel.objects.get(id=pk)
    serializer = StudentSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def studentDeleteView(request, pk):
    task = StudentModel.objects.get(id=pk)
    task.delete()
    return Response('Deleted Successfully')