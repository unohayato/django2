from django.views.generic import TemplateView

class IndexView(TemplateView):
  template_name = 'app/index.html'

class AboutView(TemplateView):
  template_name = 'app/about.html'