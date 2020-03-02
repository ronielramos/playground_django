from rest_framework import serializers, viewsets
from django.contrib.auth.models import Group, User


# Serializers define the API representation.


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
      model = User
      fields = ['url', 'name']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
      API endpoint that allows groups to be viewd or edited
    """ 
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



