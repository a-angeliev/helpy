from django.contrib.auth import mixins
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model

# Create your views here.
from project.accounts.forms import (
    CreateProfileStaffForm,
    CreateProfileHelperForm,
    DeleteProfileForm,
    EditProfileForm,
    CreateProfileRefugeeForm,
)
from project.accounts.models import Profile, ProjectUser
from project.common.view_mixins import RedirectToDashboard, TheCreatorPermissionMixin
from project.main.models import Shelter, Job

UserModel = get_user_model()

# class UserRegisterStaffView(views.CreateView):
#     form_class = CreateProfileStaffForm
#     template_name = 'accounts/profile_create_helper.html'
#     success_url = reverse_lazy('index')


class UserRegisterHelperView(RedirectToDashboard, views.CreateView):
    form_class = CreateProfileHelperForm
    template_name = "accounts/register_helper_page.html"
    success_url = reverse_lazy("index")

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['request'] = self.request
        return form_kwargs


class UserRegisterRefugeeView(RedirectToDashboard, views.CreateView):
    form_class = CreateProfileRefugeeForm
    template_name = "accounts/register_refugee_page.html"
    success_url = reverse_lazy("index")

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['request'] = self.request
        return form_kwargs
# class UserRegisterHelperView(views.CreateView):
#     form_class = CreateProfileHelperForm
#     template_name = 'accounts/profile_create_helper.html'
#     success_url = reverse_lazy('index')


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    template_name = "accounts/change_password.html"
    success_url = reverse_lazy("index")


class UserLoginView(RedirectToDashboard, auth_views.LoginView):
    template_name = "accounts/login_page.html"
    success_url = reverse_lazy("index")

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class ProfileDetailsView(
    mixins.LoginRequiredMixin, TheCreatorPermissionMixin, views.DetailView
):
    model = Profile
    template_name = "accounts/profile_details.html"
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_owner"] = self.object.user_id == self.request.user.id
        own_shelters = Shelter.objects.all().filter(user_id=self.request.user.id)
        own_jobs = Job.objects.all().filter(user_id=self.request.user.id)
        context["own_shelters"] = own_shelters
        context["own_jobs"] = own_jobs
        return context


class ProfileEditView(
    mixins.LoginRequiredMixin, TheCreatorPermissionMixin, views.UpdateView
):
    template_name = "accounts/profile_edit.html"
    form_class = EditProfileForm
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_owner"] = self.object.user_id == self.request.user.id
        return context

    def get_success_url(self):
        return reverse_lazy("profile details", kwargs={"pk": self.object.pk})


class ProfileDeleteView(
    mixins.LoginRequiredMixin, TheCreatorPermissionMixin, views.DeleteView
):
    template_name = "accounts/profile_delete.html"
    form_class = DeleteProfileForm
    model = UserModel
    success_url = reverse_lazy("index")

    # def get_queryset(self):
    #     pass
