from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedIdentityField
from .models import Group, Student


class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'student')


class StudentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

