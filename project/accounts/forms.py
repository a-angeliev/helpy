from django.contrib.auth import forms as auth_forms, login
from django import forms


from project.accounts.models import Profile
from project.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin

UserModel = auth_forms.get_user_model()


class CreateProfileFormAbstract(BootstrapFormMixin, auth_forms.UserCreationForm):
    IS_STAFF = False
    IS_SUPERUSER = False
    IS_HELPER = False
    IS_REFUGEE = False

    first_name = forms.CharField(max_length=Profile.FIRST_NAME_MAX_LENGTH)
    last_name = forms.CharField(max_length=Profile.LAST_NAME_MAX_LENGTH)
    profile_image = forms.ImageField()
    phone_number = forms.IntegerField()
    date_of_birth = forms.DateField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "YYYY-MM-DD",
            }
        )
    )
    gender = forms.ChoiceField(
        choices=Profile.GENDERS,
    )
    about_yourself = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 4,
            }
        )
    )

    def __init__(self,request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)
        user.is_staff = self.IS_STAFF
        user.is_superuser = self.IS_SUPERUSER
        user.is_helper = self.IS_HELPER
        user.is_refugee = self.IS_REFUGEE
        user.save()

        profile = Profile(
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
            profile_image=self.cleaned_data["profile_image"],
            phone_number=self.cleaned_data["phone_number"],
            date_of_birth=self.cleaned_data["date_of_birth"],
            gender=self.cleaned_data["gender"],
            about_yourself=self.cleaned_data["about_yourself"],
            user=user,
        )

        if commit:
            profile.save()
            auth_user = auth_forms.authenticate(
                username=self.cleaned_data['email'],
                password=self.cleaned_data['password1']
            )
            login(self.request, auth_user)
        return user

    class Meta:
        model = auth_forms.get_user_model()
        fields = (
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "profile_image",
            "phone_number",
            "date_of_birth",
            "gender",
            "about_yourself",
        )



class CreateProfileStaffForm(CreateProfileFormAbstract):
    IS_STAFF = True


class CreateProfileHelperForm(CreateProfileFormAbstract):
    IS_HELPER = True


class CreateProfileRefugeeForm(CreateProfileFormAbstract):
    IS_REFUGEE = True


class CreateProfileSuperuserForm(CreateProfileFormAbstract):
    IS_STAFF = True
    IS_HELPER = True
    IS_REFUGEE = True
    IS_SUPERUSER = True


class DeleteProfileForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = UserModel
        fields = ()


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        exclude = ("user", "profile_image")
