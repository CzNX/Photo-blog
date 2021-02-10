from django.urls import path, include
from . views import index, detail, create, update, delete

urlpatterns = [
    path('', index),
    path('detail/<int:id>', detail),
    path('create/', create, name="create"),
    path('update/<int:id>', update),
    path('delete/<int:id>', delete),

]
