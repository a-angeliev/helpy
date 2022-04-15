
from django.views import generic as views


class Custom404View(views.TemplateView):
    template_name = "errors/error404.html"


class Custom403View(views.TemplateView):
    template_name = "errors/error403.html"
