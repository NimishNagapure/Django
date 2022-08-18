from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import CheckList, CheckListItem


class CheckListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckListItem
        fields ='__all__'



class CheckListsSerializer(serializers.ModelSerializer):
    items =CheckListItemSerializer(source='checklistitem_set',many=True,read_only=True)
    class Meta:
        model = CheckList
        fields = '__all__'