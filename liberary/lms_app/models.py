from django.db import models
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.name or 'Unnamed Category'
class Book(models.Model):
    status_book=[('available','available'),('rental','rental'),('sold','sold'),]
    book_name=models.CharField(max_length=250,blank=True, null=True)
    author=models.CharField(max_length=250,blank=True, null=True)
    book_image=models.ImageField(upload_to='photos',null=True,blank=True)
    author_image=models.ImageField(upload_to='photos',null=True,blank=True)
    pages=models.IntegerField(null=True,blank=True)
    price=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    rental_price_day=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    total_rental=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    rental_period=models.IntegerField(blank=True, null=True)
    active=models.BooleanField(default=True)
    status=models.CharField(max_length=50,choices=status_book,blank=True, null=True)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,blank=True, null=True)

