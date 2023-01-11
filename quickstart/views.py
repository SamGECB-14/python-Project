from .models import employee
from rest_framework import generics
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from quickstart.serializers import UserSerializer, GroupSerializer , EmployeeSerializer
from rest_framework import status
from django.http import Http404


class Employeelist(generics.ListCreateAPIView):

    queryset = employee.objects.all()
    serializer_class = EmployeeSerializer

# class EmployeeDetails(generics.)


# class Employeelist(APIView):
#
#      def get(self,request, format=None):
#
#          employies = employee.objects.all()
#          serializer = EmployeeSerializer(employies,many=True)
#          return Response(serializer.data)
#
#      def post(self, request, format=None):
#
#           serializer = EmployeeSerializer(data=request.data)
#           serializer.is_valid(raise_exception=True)
#           serializer.save()
#           return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
#
# class EmployeeDetails(APIView):
#
#      def get_object(self, pk):
#          try:
#              return employee.objects.get(pk=pk)
#          except employee.DoesNotExist:
#              raise Http404
#
#      def delete(self, request, pk, format=None):
#          employies = self.get_object(pk)
#          employies.delete()
#          return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


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


