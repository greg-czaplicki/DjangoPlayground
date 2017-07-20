from django.db.models import Q
from django.views.generic import TemplateView, ListView, DetailView

from .models import RestaurantLocation


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'


class RestaurantListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        print(slug)
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) or
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

    def get_context_data(self, **kwargs):
        context = super(RestaurantDetailView, self).get_context_data(**kwargs)
        return context
