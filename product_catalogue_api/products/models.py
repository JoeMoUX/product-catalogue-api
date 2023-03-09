from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
# Create your models here.

def upload_to(instance, filename):
  return f'static/{filename}'

class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.50'))])
  quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
  image = models.ImageField(null=True, blank=True, upload_to=upload_to)
  
  def __str__(self) -> str:
    return self.name