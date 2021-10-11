from . import views
from django.urls import path
urlpatterns = [
    path('api/users/', views.user_list),
    path('api/users/<int:pk>/', views.user_detail),

    path('api/clients/', views.client_list),
    path('api/clients/<int:pk>', views.client_detail),

    path('api/cars/', views.car_list),
    path('api/cars/<int:pk>', views.car_detail),

    path('api/orders/', views.order_list),
    path('api/orders/<int:pk>', views.order_detail),

    path('api/ext_orders/', views.ext_order_list),
    path('api/ext_orders/<int:pk>', views.ext_order_detail),

    path('api/num-of-orders/<int:pk>/', views.num_of_orders),
    path('api/total-profit/<int:pk>/', views.car_total_profit),
    path('api/num-extended/<int:pk>/', views.num_extended),
    path('api/client-total/<int:pk>/', views.client_total)
    

]