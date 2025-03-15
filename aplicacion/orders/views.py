from django.views.generic import DetailView
from .models import Order
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/my_orders.html'
    context_object_name = "order"

    def get_object(self, queryset = None):
        user_actual = self.request.user
        return Order.objects.filter(user = user_actual, is_active=True).last()