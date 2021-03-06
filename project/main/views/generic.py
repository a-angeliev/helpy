from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as views

from project.common.view_mixins import RedirectToDashboard


class HomeView(RedirectToDashboard, views.TemplateView):
    template_name = "main/generic/home_page.html"


class ProvideHelpInfoView(RedirectToDashboard, views.TemplateView):
    template_name = "main/generic/provide_help_info.html"


class RegisterAsView(RedirectToDashboard, views.TemplateView):
    template_name = "main/generic/register_as.html"


class FindHelpInfoView(RedirectToDashboard, views.TemplateView):
    template_name = "main/generic/find_help.html"


class LoggedHomeView(LoginRequiredMixin, views.TemplateView):
    template_name = "main/generic/logged_home.html"


