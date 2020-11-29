from django.shortcuts import render
from django.views.generic import TemplateView
from . import clean_program
# Create your views here.

class IndexView(TemplateView):
    template_name = 'coronaApp/index.html'
    def __init__(self):
        inf = clean_program.inf_contries()
        safe = clean_program.safe_places()
        self.inf = inf
        self.safe = safe

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView,self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['inf_contries'] = self.inf
        context['safe_contries'] = self.safe
        return context
