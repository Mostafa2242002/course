from django import forms
from .models import *
class categoryform(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name',]
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'})
     }
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'book_name',
            'author',
            'book_image',
            'author_image',
            'pages',
            'price',
            'rental_price_day',
            'rental_period',
            'total_rental',
            'status',
            'category',
        ]
        widgets={
            'book_name':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'book_image':forms.FileInput(attrs={'class':'form-control'}),
            'author_image':forms.FileInput(attrs={'class':'form-control'}),
            'pages':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'rental_price_day':forms.NumberInput(attrs={'class':'form-control',"id":"rentalprice"}),
            'total_rental':forms.NumberInput(attrs={'class':'form-control',"id":"totalrental"}),
            'rental_period':forms.NumberInput(attrs={'class':'form-control',"id":"rentalperiod"}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }
