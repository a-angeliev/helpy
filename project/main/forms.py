from django import forms

from project.accounts.models import Profile
from project.common.helpers import BootstrapFormMixin
from project.main.models import Shelter, Job


class CreateShelterForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):

        shelter = super().save(commit=False)

        shelter.user = Profile.objects.filter(pk=self.user.id)[0]
        if commit:
            shelter.save()

        return shelter

    class Meta:
        model = Shelter
        exclude = ("user",)


class CreateJobForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):

        job = super().save(commit=False)

        job.user = Profile.objects.filter(pk=self.user.id)[0]
        if commit:
            job.save()

        return job

    class Meta:
        model = Job
        exclude = ("user",)


class EditShelterForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Job
        exclude = ("user",)