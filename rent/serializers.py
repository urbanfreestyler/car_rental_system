from decimal import Clamped
from django.db.models import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""                                                                   ""
""                          API FOR CLIENTS ↓                        ""
""                                                                   ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'passport_series', 'firstname', 'lastname', 'phone')
    
    def create(self, validated_data):
            client = Client.objects.create_client(validated_data['passport_series'], validated_data['firstname'], validated_data['lastname'], validated_data['phone'])

            return client




"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""                                                                   ""
""                          API FOR CARS   ↓                         ""
""                                                                   ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'brand', 'model', 'rent_cost')
    def create(self, validated_data):
            car = Car.objects.create_car(validated_data['brand'], validated_data['model'], validated_data['rent cost'])

            return car




"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""                                                                   ""
""                          API FOR ORDERS  ↓                        ""
""                                                                   ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'client_id', 'car_id', 'from_date', 'to_date')




"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""                                                                   ""
""                          API FOR USERS ↓                          ""
""                                                                   ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)
        
        def create(self, validated_data):
            user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

            return user




"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""                                                                   ""
""                  API FOR EXTENDED ORDERS ↓                        ""
""                                                                   ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



class ExtendedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extended_order
        fields = ('id', 'order', 'new_to_date',)

        def create(self, validated_data):
            new_to_date = Extended_order.objects.create_extended_orders(validated_data['order'], validated_data['new_to_date'])

            return new_to_date

