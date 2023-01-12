from .models import employee
from rest_framework import generics
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from quickstart.serializers import UserSerializer, GroupSerializer , EmployeeSerializer,EmployeeListSerializer
from rest_framework import status
from django.http import Http404





# VIEWS SET
class EmployeeListViewSet(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = EmployeeListSerializer
    permission_classes = [permissions.IsAuthenticated]




# GENERIC API VIEW
class Employeelist(generics.ListCreateAPIView):
    queryset = employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class EmployeeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request,*args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




# API VIEWS
class Employee1list(APIView):

     def get(self,request, format=None):

         employies = employee.objects.all()
         serializer = EmployeeSerializer(employies,many=True)
         return Response(serializer.data)

     def post(self, request, format=None):

          serializer = EmployeeSerializer(data=request.data)
          serializer.is_valid(raise_exception=True)
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)

class Employee1Details(APIView):

     def get_object(self, pk):
         try:
             return employee.objects.get(pk=pk)
         except employee.DoesNotExist:
             raise

     def get(self, request, pk):
         employies = self.get_object(pk)
         serializer = EmployeeSerializer(employies)
         return Response(serializer.data)

     def put(self, request,pk):
         employies = self.get_object(pk)
         serializer = EmployeeSerializer(employies, data=request.DATA)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     def delete(self, request,pk):
         employies = self.get_object(pk)
         employies.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)





class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


