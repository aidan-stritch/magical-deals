from django.forms import ModelForm
from .models import Product


class ProductCreationForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'price', 'image']
