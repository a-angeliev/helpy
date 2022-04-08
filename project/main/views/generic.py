from django.shortcuts import redirect
from django.views import generic as views


class HomeView(views.TemplateView):
    template_name = 'main/home_page.html'



class ProvideHelpInfoView(views.TemplateView):
    template_name = "main/provide_help_info.html"


class RegisterAsView(views.TemplateView):
    template_name = "main/register_as.html"


# LoginRequiredMixin --> give access if user is loged