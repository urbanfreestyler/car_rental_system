from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils import timezone


# Create your models here.


class Client(models.Model):
    passport_series = models.CharField(max_length=120)
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)

    def __str__(self):
        return self.firstname + " " + self.lastname


class Car(models.Model):
    brand = models.CharField(max_length=120)
    model = models.CharField(max_length=120)
    rent_cost = models.PositiveIntegerField(default=10)
    
    def __str__(self):
        return self.brand + " " + self.model


class Order(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    from_date = models.DateTimeField(default=datetime.today())
    to_date = models.DateTimeField(default=datetime.today())

    ext_num = models.IntegerField(default=0, help_text="This field changes automatically, just skip this field.")


    def save(self, *args, **kwargs):
        now = timezone.now()
        if self.to_date < now:
            raise ValidationError("The date can't be in the past!")
        elif self.to_date < self.from_date:
            raise ValidationError("to_date can't be earlier than from_date!")
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)



class Extended_order(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    new_to_date = models.DateTimeField(default=datetime.now())

    orders = Order.objects.all()

    def update(self, *args, **kwargs):
        ext_order = Order.objects.get(id = self.orders)
        to_date = ext_order.to_date
        if self.new_to_date > to_date:
            to_date = self.new_to_date

            ext_order.ext_num += 1

            super(Order, self).save(args, **kwargs)
    
    def __int__(self):
        return (self.id)






