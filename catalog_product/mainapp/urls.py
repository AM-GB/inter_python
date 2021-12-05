from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('category/<int:pk>/', mainapp.category, name='category'),
    path('create/', mainapp.ProductCreate.as_view(),
         name='product_create'),

]
