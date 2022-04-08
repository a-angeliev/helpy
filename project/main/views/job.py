from django.contrib.auth import mixins
from django.urls import reverse_lazy
from django.views import generic as views

from project.accounts.models import Profile
from project.main.forms import CreateJobForm
from project.main.models import Job


class CreateJobView(mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'main/create_job.html'
    form_class = CreateJobForm
    success_url = reverse_lazy('index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditJobView(views.UpdateView):
    template_name = "main/edit_job.html"
    model = Job
    fields = ("title", "description", "money", "is_total", "city",)


class DetailsJobView(views.DetailView):
    template_name = "main/details_job.html"
    model = Job

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        creator = Profile.objects.filter(pk=self.object.user.id)
        if creator:
            context['creator'] = creator[0]
        return context


class AllJobView(views.ListView):
    template_name = 'main/all_jobs.html'
    model = Job
    context_object_name = 'jobs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context