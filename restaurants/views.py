from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context = {
            'name': 'Greg'
        }
        return context
