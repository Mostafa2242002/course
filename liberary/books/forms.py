from django import forms
from .models import *
class categoryform(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'})
     }
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'book_image',
            'author_image',
            'pages',
            'price',
            'rental_price_day',
            'rental_period',
            'status',
            'category',
        ]
        widgets={
            # 'title':forms.TextInput(attrs={'class':'form'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'book_image':forms.FileInput(attrs={'class':'form-control'}),
            'author_image':forms.FileInput(attrs={'class':'form-control'}),
            'pages':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'rental_price_day':forms.NumberInput(attrs={'class':'form-control'}),
            'rental_period':forms.NumberInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }
