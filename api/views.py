from django.shortcuts import render
from rest_framework.status import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAdminUser,AllowAny
from rest_framework.response import Response
from .permissions import CustomUserPermission,CustomUserDetailPermission,ProjectPermission,ProjectDetailPermission,TaskPermission,TaskDetailPermission
from app.models import CustomUser,Project,Task
from .serializers import CustomUserSerializer,ProjectSerializer,TaskSerializer

@api_view(['GET','POST'])
@permission_classes([CustomUserPermission])

def custom_user(request):
    user = CustomUser.objects.all()
    if request.method == 'GET':
        serializer = CustomUserSerializer(user,many = True,context = {'request':request})
        return Response(serializer.data,status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CustomUserSerializer(data= request.data,context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes([CustomUserDetailPermission])

def custom_user_detail(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = CustomUserSerializer(user,context = {'request':request})
        return Response(serializer.data,status=HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CustomUserSerializer(data= request.data,context = {'request':request},partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
@permission_classes([ProjectPermission])

def project(request):
    project = Project.objects.all()
    if request.method == 'GET':
        serializer = ProjectSerializer(project,many = True,)
        return Response(serializer.data,status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ProjectSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes([ProjectDetailPermission])

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data,status=HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProjectSerializer(data= request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        project.delete()
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    


@api_view(['GET','POST'])
@permission_classes([TaskPermission])

def task(request):
    task = Task.objects.all()
    if request.method == 'GET':
        serializer = TaskSerializer(task,many = True,context = {'request':request})
        return Response(serializer.data,status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TaskSerializer(data= request.data,context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes([TaskDetailPermission])

def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data,status=HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = TaskSerializer(data= request.data,context = {'request':request},partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(serializer.errors,status=HTTP_204_NO_CONTENT)