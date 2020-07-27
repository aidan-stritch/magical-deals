from django.forms import ModelForm
from .models import Review


class reviewCreationForm(ModelForm):
    class Meta:
        model = Review
        fields = ['description', 'rating']
