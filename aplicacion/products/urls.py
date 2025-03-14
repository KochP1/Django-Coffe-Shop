from django.urls import path
from .views import ProductFormView, ProductShowView

urlpatterns = [
    path('', ProductShowView.as_view(), name="show_product"),
    path('agregar/', ProductFormView.as_view(), name="add_product")
]