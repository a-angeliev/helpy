from django.contrib.auth import mixins
from django.urls import reverse_lazy
from django.views import generic as views

from project.accounts.models import Profile
from project.common.view_mixins import TheCreatorPermissionMixin
from project.main.forms import CreateJobForm, EditJobForm
from project.main.models import Job


class CreateJobView(mixins.LoginRequiredMixin, views.CreateView):
    template_name = "main/job/create_job.html"
    form_class = CreateJobForm
    success_url = reverse_lazy("index")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class EditJobView(
    mixins.LoginRequiredMixin, TheCreatorPermissionMixin, views.UpdateView
):
    template_name = "main/job/edit_job.html"
    form_class = EditJobForm
    model = Job

    def get_success_url(self, *kwargs):
        return reverse_lazy("profile details", kwargs={"pk": self.request.user.id})

    # fields = ("title", "description", "money", "compensation", "city",)

    # def test_func(self):
    #     return self.get_object().user_id == self.request.user.id


class DetailsJobView(
    mixins.LoginRequiredMixin, TheCreatorPermissionMixin, views.DetailView
):
    template_name = "main/job/details_job.html"
    model = Job

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        creator = Profile.objects.filter(pk=self.object.user.id)
        if creator:
            context["creator"] = creator[0]
        return context


class DeleteJobView(
    mixins.LoginRequiredMixin, TheCreatorPermissionMixin, views.DeleteView
):
    template_name = "main/job/delete_job.html"
    model = Job

    def get_success_url(self, **kwargs):
        return reverse_lazy("profile details", kwargs={"pk": self.request.user.id})


class AllJobView(mixins.LoginRequiredMixin, views.ListView):
    template_name = "main/job/all_jobs.html"
    model = Job
    context_object_name = "jobs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
