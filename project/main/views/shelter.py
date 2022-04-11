from django.contrib.auth import mixins
from django.urls import reverse_lazy
from django.views import generic as views

from project.accounts.models import Profile
from project.common.helpers import BootstrapFormMixin
from project.common.view_mixins import RedirectToDashboard, TheCreatorPermissionMixin
from project.main.forms import CreateShelterForm, EditShelterForm
from project.main.models import Shelter


class CreateShelterView(mixins.LoginRequiredMixin, views.CreateView):
    template_name = "main/create_shelter.html"
    form_class = CreateShelterForm
    success_url = reverse_lazy("index")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class DetailsShelterView(views.DetailView):
    template_name = "main/details_shelter.html"
    model = Shelter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pesho"] = "pesho"
        creator = Profile.objects.filter(pk=self.object.user.id)
        if creator:
            context["creator"] = creator[0]

        return context


class EditShelterView(
    mixins.LoginRequiredMixin, TheCreatorPermissionMixin, views.UpdateView
):
    template_name = "main/edit_shelter.html"
    form_class = EditShelterForm
    model = Shelter
    # fields = ("title", "city", "description", "ppl_number", "room_number", "has_wc", "has_net", "has_kitchen", "has_tv", "has_garage",)

    # TODO: shound change link when i make details shelter page
    def get_success_url(self, *kwargs):
        return reverse_lazy("details shelter", kwargs={"pk": self.object.pk})


class DeleteShelterView(
    mixins.LoginRequiredMixin, TheCreatorPermissionMixin, views.DeleteView
):
    template_name = "main/delete_shelter.html"
    model = Shelter

    def get_success_url(self, **kwargs):
        return reverse_lazy("profile details", kwargs={"pk": self.request.user.id})


class AllSheltersView(views.ListView):
    template_name = "main/all_shelters.html"
    model = Shelter
    context_object_name = "shelter"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        print(context)
        return context
