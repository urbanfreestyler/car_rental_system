from django.shortcuts import render

from django.http import HttpResponse, JsonResponse, response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status


from django.contrib.auth.models import User
from .models import Car, Client, Order, Extended_order
from .serializers import *

from rest_framework.decorators import api_view

# Create your views here.


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""                                                                   ""
""                         VIEW FOR USERS ↓                          ""
""                                                                   ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        
        username = request.query_params.get('username', None)
        if username is not None:
            users = users.filter(username__icontains=username)
        
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)

 
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try: 
        user = User.objects.get(pk=pk) 
    except User.DoesNotExist: 
        return JsonResponse({'message': 'This user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        user_serializer = UserSerializer(user) 
        return JsonResponse(user_serializer.data) 
 
    elif request.method == 'PUT': 
        user_data = JSONParser().parse(request) 
        user_serializer = UserSerializer(user, data=user_data) 
        if user_serializer.is_valid(): 
            user_serializer.save() 
            return JsonResponse(user_serializer.data) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        user.delete() 
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""                                                                   ""
""                       VIEW FOR CLIENTS ↓                          ""
""                                                                   ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


@api_view(['GET', 'POST', 'DELETE'])
def client_list(request):
    if request.method == 'GET':
        clients = Client.objects.all()
        
        phone = request.query_params.get('phone', None)
        if phone is not None:
            clients = Client.filter(phone__icontains=phone)
        
        clients_serializer = ClientSerializer(clients, many=True)
        return JsonResponse(clients_serializer.data, safe=False)

 
    elif request.method == 'POST':
        client_data = JSONParser().parse(request)
        client_serializer = ClientSerializer(data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse(client_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Client.objects.all().delete()
        return JsonResponse({'message': '{} Clients were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, pk):
    try: 
        client = Client.objects.get(pk=pk) 
    except Client.DoesNotExist: 
        return JsonResponse({'message': 'This client does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        client_serializer = ClientSerializer(client) 
        return JsonResponse(client_serializer.data) 
 
    elif request.method == 'PUT': 
        client_data = JSONParser().parse(request) 
        client_serializer = UserSerializer(client, data=client_data) 
        if client_serializer.is_valid(): 
            client_serializer.save() 
            return JsonResponse(client_serializer.data) 
        return JsonResponse(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        client.delete() 
        return JsonResponse({'message': 'Client was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""                                                                   ""
""                         VIEW FOR ORDERS ↓                         ""
""                                                                   ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""  



@api_view(['GET', 'POST', 'DELETE'])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        
        order_id = request.query_params.get('id', None)
        if order_id is not None:
            orders = orders.filter(order_id__icontains=order_id)
        
        order_serializer = OrderSerializer(orders, many=True)
        return JsonResponse(order_serializer.data, safe=False)

 
    elif request.method == 'POST':
        order_data = JSONParser().parse(request)
        order_serializer = UserSerializer(data=order_data)
        if order_serializer.is_valid():
            order_serializer.save()
            return JsonResponse(order_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Order.objects.all().delete()
        return JsonResponse({'message': '{} Orders were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, pk):
    try: 
        order = Order.objects.get(pk=pk) 
    except Order.DoesNotExist: 
        return JsonResponse({'message': 'This order does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        order_serializer = OrderSerializer(order) 
        return JsonResponse(order_serializer.data) 
 
    elif request.method == 'PUT': 
        order_data = JSONParser().parse(request) 
        order_serializer = UserSerializer(order, data=order_data) 
        if order_serializer.is_valid(): 
            order_serializer.save() 
            return JsonResponse(order_serializer.data) 
        return JsonResponse(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        order.delete() 
        return JsonResponse({'message': 'Order was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""                                                                   ""
""                         VIEW FOR CARS ↓                           ""
""                                                                   ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


@api_view(['GET', 'POST', 'DELETE'])
def car_list(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        
        car_id = request.query_params.get('id', None)
        if car_id is not None:
            cars = cars.filter(car_id__icontains=car_id)
        
        car_serializer = CarSerializer(cars, many=True)
        return JsonResponse(car_serializer.data, safe=False)

 
    elif request.method == 'POST':
        car_data = JSONParser().parse(request)
        car_serializer = CarSerializer(data=car_data)
        if car_serializer.is_valid():
            car_serializer.save()
            return JsonResponse(car_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(car_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Car.objects.all().delete()
        return JsonResponse({'message': '{} Cars were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def car_detail(request, pk):
    try: 
        car = Car.objects.get(pk=pk) 
    except Car.DoesNotExist: 
        return JsonResponse({'message': 'This car does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        car_serializer = CarSerializer(car) 
        return JsonResponse(car_serializer.data) 
 
    elif request.method == 'PUT': 
        car_data = JSONParser().parse(request) 
        car_serializer = CarSerializer(car, data=car_data) 
        if car_serializer.is_valid(): 
            car_serializer.save() 
            return JsonResponse(car_serializer.data) 
        return JsonResponse(car_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        car.delete() 
        return JsonResponse({'message': 'Car was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)




"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""                                                                   ""
""                     VIEW FOR EXTENDED ORDERS ↓                    ""
""                                                                   ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


@api_view(['GET', 'POST', 'DELETE'])
def ext_order_list(request):
    if request.method == 'GET':
        ext_orders = Extended_order.objects.all()
        
        ext_orders_id = request.query_params.get('id', None)
        if ext_orders_id is not None:
            ext_orders_id = ext_orders_id.filter(ext_orders_id_icontains=ext_orders_id)
        
        extended_serializer = ExtendedSerializer(ext_orders, many=True)
        return JsonResponse(extended_serializer.data, safe=False)

 
    elif request.method == 'POST':
        extended_order_data = JSONParser().parse(request)
        extended_serializer = CarSerializer(data=extended_order_data)
        if extended_serializer.is_valid():
            extended_serializer.save()
            return JsonResponse(extended_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(extended_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Extended_order.objects.all().delete()
        return JsonResponse({'message': '{} Extended orders were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def ext_order_detail(request, pk):
    try: 
        ext_order = Extended_order.objects.get(pk=pk) 
    except Extended_order.DoesNotExist: 
        return JsonResponse({'message': 'This extended order does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        extended_serializer = ExtendedSerializer(ext_order) 
        return JsonResponse(extended_serializer.data) 
 
    elif request.method == 'PUT': 
        ext_order_data = JSONParser().parse(request) 
        extended_serializer = CarSerializer(ext_order, data=ext_order_data) 
        if extended_serializer.is_valid(): 
            extended_serializer.save() 
            return JsonResponse(extended_serializer.data) 
        return JsonResponse(extended_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        ext_order.delete() 
        return JsonResponse({'message': 'Extended order was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)




"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""                                                                   ""
""                     VIEW FOR NUMBER OF ORDERS ↓                   ""
""                                                                   ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


@api_view
def num_of_orders(request):
    if request.methpd == "POST":
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')

    num = 0

    orders = Order.objects.all()
    
    num += orders.filter(selfdate__gte=date1, date__lte=date2).count()

    return num




"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""                                                                   ""
""              VIEW FOR TOTAL PROFIT OF SPECIFIC CAR ↓              ""
""                                                                   ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

@api_view
def car_total_profit(request, pk):
        car = Car.objects.get(pk=pk)

        total_profit = 0

        orders = Order.objects.all()

        for order in orders:
            if car == orders.car_id:
                total_profit += (order.to_date - order.from_date).days() * car.rent_cost
            else:
                pass
        return total_profit

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""                                                                   ""
""              VIEW FOR ORDER'S EXTENSION NUMBER ↓                  ""
""                                                                   ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


@api_view
def num_extended(request, pk):
    order = Order.objects.get(pk=pk)

    ext_orders = Extended_order.objects.all()

    num_ext = 0

    for ext_order in ext_orders:
        if order.id == ext_order.order_id:
            num_ext += 1
        else:
            pass
    return num_ext


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""                                                                   ""
""       VIEW FOR CLIENT'S TOTAL NUM OF ORDERS AND EXPENSE ↓         ""
""                                                                   ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



@api_view
def client_total(request, pk):
    client = Client.objects.get(pk=pk)

    orders = Order.objects.all()
    ext_orders = Extended_order.objects.all()

    client_num = 0
    total_cost = 0

    for order in orders:
        if client.id == order.client_id:
            client_num += 1

            total_cost += order.rent_cost * ((order.to_date - order.from_date).days())
        else:
            pass

    for ext_order in ext_orders:
        if client.id == ext_order.client_id:
            client_num += 1

            total_cost += order.rent_cost * ((ext_order.new_to_date - order.to_date).days())
        else:
            pass
    return client_num, total_cost




