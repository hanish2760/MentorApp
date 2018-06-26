

from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from rest_framework import status
from rest_framework import serializers

from onlineapp.models import Student
from onlineapp.serializers.serializersfile import StudentSerializer, StudentDetailsSerializer
from rest_framework.response import Response

class StudentList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None,*args,**kwargs):
        if 'sid' in kwargs.keys():
            try:
                student = Student.objects.get(id=kwargs['sid'])
                serializer = StudentSerializer(student)
                return Response(serializer.data,status=200)
            except Student.DoesNotExist:
                return Response({'error': 400}, status=status.HTTP_400_BAD_REQUEST)
        elif 'pk' in kwargs.keys():
            students = Student.objects.filter(college__id=kwargs['pk'])
        else:
            students = Student.objects.all()

        serializer = StudentSerializer(students, many=True)
        #ser=[serializer.data]
        #return JsonResponse(serializer.data,safe=False)
        return Response(serializer.data,status=200)
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,**kwargs):
        try:
            std = Student.objects.get(id=kwargs['sid'])#.filter(college__id = kwargs['id'])
        except Student.DoesNotExist:
            return Response({'error': 400}, status=status.HTTP_400_BAD_REQUEST)

        request.data['college'] = kwargs['id']


        serializer = StudentDetailsSerializer(std, data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):

        try:
            std = Student.objects.get(id=kwargs['sid'])  # .filter(college__id = kwargs['id'])
        except Student.DoesNotExist:
            return Response({'error': 400}, status=status.HTTP_400_BAD_REQUEST)

        std.delete()
        return Response({}, status=status.HTTP_200_OK)




