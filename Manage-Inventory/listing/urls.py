from django.urls import path
from .views import dashboard, add, list_pdt, edit, delete
urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('add/', add, name="add"),
    path('list/', list_pdt, name="list"),    
    path('edit/<int:unique_id>/', edit, name="edit"),
    path('delete/<int:unique_id>/', delete, name="delete"),
]
