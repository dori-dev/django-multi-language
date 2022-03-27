"""user profile view
"""
from django.views.generic import TemplateView


class IndexPage(TemplateView):
    template_name = "index.html"
