from django.db import models

# Create your models here.

class Customer(models.Model):
    id_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Product(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    sale_value = models.DecimalField(max_digits=10, decimal_places=2)
    handles_vat = models.BooleanField(default=False)
    vat_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

class SaleHeader(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(auto_now_add=True)
    total_sale = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_number = models.CharField(max_length=20, unique=True)

class SaleDetail(models.Model):
    sale_header = models.ForeignKey(SaleHeader, related_name='details', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)