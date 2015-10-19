from django.views.generic import TemplateView
import os.path
Temp_Path = os.path.realpath('.')

class Index(TemplateView):
    template_name = "template.html"