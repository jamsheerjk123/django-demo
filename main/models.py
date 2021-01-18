from django.db import models

class ProductModel(models.Model):
    name=models.CharField(max_length=60,unique=True,null=False,blank=True)
    price=models.PositiveIntegerField()
    description=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='product_table'
        unique_together:list
        unique_together:['name','description']

class ProductModelForm(forms.Modelform):
