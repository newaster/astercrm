from rest_framework import serializers
#from .models import User
from .models import Software

from astercrm.models import Subscription,Sales

class softwareSerializer(serializers.ModelSerializer):

    class Meta:
        model = Software
        fields = '__all__'




class subscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ['last_login']




class salesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sales
        fields = '__all__'