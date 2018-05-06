import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import TestForm, TestForm2


class HomeView(TemplateView):
    template_name = 'test_app/home.html'


class AjaxTemplateMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'ajax_template_name'):
            split = self.template_name.split('.html')
            split[-1] = '_inner'
            split.append('.html')
            self.ajax_template_name = ''.join(split)
        if request.is_ajax():
            self.template_name = self.ajax_template_name
            try:
                if kwargs['pk']=='b|t|':
                    # self.form_class = TestForm2
                    self.initial = {'name':'TESTTTT'}
            except:
                pass
        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)



class TestFormView(SuccessMessageMixin, AjaxTemplateMixin, FormView):
    template_name = 'test_app/test_form.html'
    form_class = TestForm
    success_url = reverse_lazy('home')
    success_message = "Way to go!"

    def form_valid(self, form):
        html = render_to_string('test_app/test_form_success.html', {'news': {'title' : 'test'}})
        response = {'status': True, 'form': html}
        # messages.info(self.request,self.success_message)
        return JsonResponse(response)
        # return render(self.request, 'test_app/test_form_success.html', {'news': 1})
