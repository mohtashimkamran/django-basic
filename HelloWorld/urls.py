from django.urls import path

#every url file should contain a variable named urlpatterns

from HelloWorld import views

urlpatterns = [
    path('',views.index),
    path("hello",views.hello2)
]