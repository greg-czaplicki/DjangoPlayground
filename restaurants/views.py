from django.db.models import Q
from django.views.generic import TemplateView, ListView

from .models import RestaurantLocation


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'


class RestaurantListView(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) or
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset
