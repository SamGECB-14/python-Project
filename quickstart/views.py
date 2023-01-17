from .models import employee,Student , Song,Singer
from rest_framework import generics
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import permissions
from quickstart.serializers import UserSerializer, GroupSerializer , EmployeeSerializer,EmployeeListSerializer
from quickstart.serializers import SongSerializer,SingerSerializer,StudentSerializer
from rest_framework import status
from django.http import Http404
from rest_framework import filters
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django_filters.rest_framework import DjangoFilterBackend



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username


        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET', 'POST'])
def student_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        st = Student.objects.all()
        serializer = StudentSerializer(st, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        st = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(st)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(st, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        st.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class studentlist(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        st = Student.objects.all()
        serializer = StudentSerializer(st, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class studentdetails(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        st = self.get_object(pk)
        serializer = StudentSerializer(st)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        st = self.get_object(pk)
        serializer = StudentSerializer(st, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        st = self.get_object(pk)
        st.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'city']


# VIEWS SET
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = EmployeeListSerializer





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


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated]



class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'email','song',]

