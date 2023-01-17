from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import employee , Student, Song,Singer



class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    rol_number = serializers.IntegerField()
    city = serializers.CharField(max_length=200)

    def create(self, validated_data):
           """
           Create and return a new `Snippet` instance, given the validated data.
           """
           return Student(**validated_data)

    def update(self, instance, validated_data):
           """
           Update and return an existing `Snippet` instance, given the validated data.
           """
           instance.name = validated_data.get('name', instance.name)
           instance.rol_number = validated_data.get('rol_number', instance.rol_number)
           instance.city = validated_data.get('city', instance.city)
           instance.save()
           return instance

class StudentSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    class Meta:
        model = Student
        fields = ('id','url','name','rol_number','city')
        # depth = 1# For Relationshik Keys


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = ('id','firstname','lastname','emp_id')

class EmployeeListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = employee
        fields = ('url','id','firstname','lastname','emp_id')


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        # singer = Singer.objects.filter(namee = 'pk')
        fields = ['name','release_date','singer']


class SingerSerializer(serializers.ModelSerializer):
    song = SongSerializer(many=True,read_only=True)

    class Meta:
        model = Singer
        fields = ['id','name', 'email','photo', 'song']

