from django.db import models
from autoslug import AutoSlugField
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------

class Category(models.Model):
    category_name=models.CharField(max_length=100,null=False)
    category_slug=AutoSlugField(populate_from="category_name",unique=True)

    def __str__(self):
        return self.category_name

# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------


class ProductCustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
    def royalCanin(self):
        return super().get_queryset().filter(product_brand="Royal Canin")
    
    def drools(self):
        return super().get_queryset().filter(product_brand="drools")

# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------


# Create your models here.
# Step 1:Create class which inherits Model class From models
class Product(models.Model):

    product_name=models.CharField(max_length=100,null=False)
    product_description=models.TextField(default=" product description")
    product_price=models.PositiveIntegerField(default=0)
    product_image=models.ImageField(upload_to="products/")
    product_brand=models.CharField(max_length=100,default="superpet")

    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)

    riya=models.Manager()
    customManager=ProductCustomManager()
    
    def __str__(self):
        return self.product_name
    
       
   
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
