from django.db import models
from django.contrib.auth.models import User
import datetime
import os

def get_file_path(reqest, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:&M:&S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/',filename)

# ใช้สร้าง table class = table migrations -> migrate

class Category(models.Model):
    slug = models.CharField(max_length=150, null= False,blank=False)
    name = models.CharField(max_length=150, null= False,blank=False)
    image = models.ImageField(upload_to=get_file_path, null= False,blank=False)
    description = models.TextField(max_length=500, null= False,blank=False)
    status = models.BooleanField(default= False, help_text="0=default ,1=Hidden")
    trending = models.BooleanField(default= False, help_text="0=default ,1=Hidden")
    meta_title = models.CharField(max_length=150, null= False,blank=False)
    meta_keywords = models.CharField(max_length=150, null= False,blank=False)
    meta_description = models.TextField(max_length=500, null= False,blank=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null= False,blank=False)
    name = models.CharField(max_length=150, null= False,blank=False)
    Product_image = models.ImageField(upload_to=get_file_path, null= False,blank=False)
    small_description = models.CharField(max_length=250, null= False,blank=False)
    quantity = models.IntegerField(null=False,blank=False)
    description = models.TextField(max_length=500, null= False,blank=False)
    original_price = models.FloatField(null=False,blank=False)
    selling_price = models.FloatField(null=False,blank=False)
    status = models.BooleanField(default= False, help_text="0=default ,1=Hidden")
    trending = models.BooleanField(default= False, help_text="0=default ,1=Hidden")
    tag = models.CharField(max_length=150, null= False,blank=False)
    meta_title = models.CharField(max_length=150, null= False,blank=False)
    meta_keywords = models.CharField(max_length=150, null= False,blank=False)
    meta_description = models.TextField(max_length=500, null= False,blank=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False,blank=False)
    created_at = models.DateField(auto_now_add=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=150,null=False)
    lname = models.CharField(max_length=150,null=False)
    email = models.CharField(max_length=150,null=False)
    phone = models.CharField(max_length=150,null=False)
    total_price = models.FloatField(max_length=150,null=False)
    payment_mode = models.CharField(max_length=150,null=False)
    payment_id = models.CharField(max_length=140,null=False)
    redeem_code = models.CharField(max_length=150,null=True)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self) -> str:
        return '{} - {}'.format(self.id, self.redeem_code)
    
class OrderItem(models.Model):
    order = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    def __str__(self) -> str:
        return '{} - {}'.format(self.order.id, self.order.redeem_code)
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.CharField(max_length=150,null=False)
    phone = models.CharField(max_length=150,null=False)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self) -> str:
        return self.user.username
