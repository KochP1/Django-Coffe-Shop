from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from .forms import ProductForm
from .models import Product

class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy('add_product')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProductShowView(TemplateView):
    template_name = "products/show_products.html"

    def get_context_data(self):
        prod_list = Product.objects.all()

        return {
            'prod_list': prod_list
        }
