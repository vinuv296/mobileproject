from django.db import models

# Create your models here.


class Brand(models.Model):
    brand_name=models.CharField(max_length=120,unique=True)

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    mobile_name=models.CharField(max_length=120,unique=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    price=models.IntegerField()
    spec=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images")

    def __str__(self):
        return self.mobile_name


class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.CharField(max_length=120)
    options=(("ordernotplaced","ordernotplaced"),
             ("orderplaced","orderplaced"))
    status=models.CharField(max_length=120,choices=options,default="ordernotplaced")


class Orders(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.CharField(max_length=120)
    address=models.CharField(max_length=200)
    options=(("ordered","ordered"),
             ("packed","packed"),
             ("shipped","shipped"),
             ("delivered","delivered"),
             ("cancelled","cancelled")
             )
    status=models.CharField(max_length=120,choices=options,default="ordered")
    date=models.DateField(auto_now=True)