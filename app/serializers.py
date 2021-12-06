from .models import CountryModel
from rest_framework import serializers
class CountrySeriliazers(serializers.ModelSerializer):
    class Meta:
        model=CountryModel
        fields="__all__"