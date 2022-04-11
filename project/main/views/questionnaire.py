from django.urls import reverse_lazy
from django.views import generic as views

from project.main.forms import CreateQuestionForm
from project.main.models import Questionnaire


class CreateQuestionnaireView(views.CreateView):
    template_name = "main/questionnaire/create_questionnaire.html"
    form_class = CreateQuestionForm
    success_url = reverse_lazy("index")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class ALlQuestionnaireView(views.ListView):
    template_name = "main/questionnaire/list_questionnaire.html"
    model = Questionnaire
