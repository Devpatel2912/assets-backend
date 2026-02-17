from django.db import models

class UserMasters(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50)

    class Meta:
        db_table = 'user_masters'


class DeptMasters(models.Model):
    did = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'dept_masters'
       


class CategoryMasters(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'category_msters'



class ProductMasters(models.Model):
    productid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    quantity = models.IntegerField()
    dimensions = models.CharField(max_length=100, null=True)
    cid = models.IntegerField()
    description = models.CharField(max_length=255, null=True)
    did = models.IntegerField()
    createat = models.DateTimeField()
    updateat = models.DateTimeField()

    class Meta:
        db_table = 'product_masters'
       


class StorageMasters(models.Model):
    storageid = models.AutoField(primary_key=True)
    productid = models.IntegerField()
    lid = models.IntegerField()
    did = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField(null=True)
    createat = models.DateTimeField()
    updateat = models.DateTimeField()

    class Meta:
        db_table = 'storage_masters'
       

class ProductImageMasters(models.Model):
    id = models.AutoField(primary_key=True)
    productid = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')
    create_at = models.DateTimeField()

    class Meta:
        db_table = 'productimage_masters'
        
class DeptMasters(models.Model):
    did = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    userid = models.IntegerField()
    remark = models.CharField(max_length=255, null=True, blank=True)

    createAT = models.DateTimeField(db_column='createat')
    updateAT = models.DateTimeField(db_column='updateat')

    class Meta:
        db_table = 'dept_masters'
     

class LocationMasters(models.Model):
    lid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    did = models.IntegerField()
    description = models.TextField(null=True, blank=True)

    createAT = models.DateTimeField(db_column='createat')
    updateAT = models.DateTimeField(db_column='updateat')

    class Meta:
        db_table = 'location_masters'
   