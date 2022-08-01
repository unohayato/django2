from django.views.generic import TemplateView

class IndexView(TemplateView):
  template_name = 'app/index.html'

  def get_context_data(self):
    ctxt = super().get_context_data()
    ctxt['username'] = ''
    return ctxt

class AboutView(TemplateView):
  template_name = 'app/about.html'
  def get_context_data(self):
    ctxt = super().get_context_data()
    ctxt['num_services'] = 123456789
    ctxt['skills'] = [
      'Python',
      'Javascript',
      'Rust',
      'PHP',
      'C++'
    ]
    return ctxt
  
  