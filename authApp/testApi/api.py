from django.contrib.auth.models import User
from avatar.models import Avatar
from tastypie import fields
from tastypie.resources import ModelResource
from testApi.models import FoodOption, Vote
from tastypie.serializers import Serializer
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication
from tastypie.constants import ALL, ALL_WITH_RELATIONS

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        serializer = Serializer(formats=['jsonp', 'json'])
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        trailing_slash = False
        fields = ['username','id']
        
class AvatarResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', full=True)
    
    class Meta:
        queryset = Avatar.objects.all()
        resource_name = 'avatar'
        serializer = Serializer(formats=['jsonp', 'json'])
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        trailing_slash = False
        filtering = {
            "user": ('exact'),
        }

class FoodResource(ModelResource):
    class Meta:
        queryset = FoodOption.objects.all()
        resource_name = 'food'
        serializer = Serializer(formats=['jsonp', 'json'])
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        trailing_slash = False

class VoteResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', full=True)
    food_option = fields.ForeignKey(FoodResource, 'food_option', full=True)

    class Meta:
        queryset = Vote.objects.all()
        filtering = {
            "food_option": ('exact'),
            "user": ('exact'),
        }
        resource_name = 'vote'
        serializer = Serializer(formats=['jsonp', 'json'])
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        trailing_slash = False