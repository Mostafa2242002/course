from . import views
from django.urls import  path
urlpatterns = [
    path("",views.home_page,name="index"),
    path("books/",views.books,name="books"),
    path("update/<int:id>",views.update,name="updater"),
    path('delete/<int:id>',views.delete_book,name="delete"),

]
