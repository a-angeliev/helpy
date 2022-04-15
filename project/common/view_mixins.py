
from django.contrib.auth import mixins
from django.http import Http404
from django.shortcuts import redirect

from project.main.models import Questionnaire


class RedirectToDashboard:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("logged")

        return super().dispatch(request, *args, **kwargs)


class TheCreatorPermissionMixin(mixins.UserPassesTestMixin):
    def test_func(self):
        return self.get_object().user_id == self.request.user.id


class RedirectToQuestionnaire:
    def dispatch(self, request, *args, **kwargs):
        if not Questionnaire.objects.filter(user_id=request.user.id).exists():
            return redirect("create questionnaire")

        return super().dispatch(request, *args, **kwargs)

