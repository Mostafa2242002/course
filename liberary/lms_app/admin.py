from django.contrib import admin
from .models import *
# Register your models here.
class Book_table(admin.ModelAdmin):
    list_display= [ 'book_name','author','book_image','author_image','pages','price','rental_price_day']
    list_display_links=['book_name']
    list_editable=[ 'author','book_image','author_image','pages','price','rental_price_day']
class Category_table(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    list_editable = []

    def display_related_books(self, obj):
        return ", ".join([str(book) for book in obj.rel.all()])
    display_related_books.short_description = 'Related Books'

admin.site.register(Category,Category_table)#, Category_table)
admin.site.register(Book,Book_table)#,Book_table)
