from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("contacts/", views.contacts, name="contact"),
    path("contacts/edit/<int:id>", views.edit, name="edit"),
    path("contacts/delete/<int:id>", views.delete, name="delete"),

]