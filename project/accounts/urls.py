from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from project.accounts.views import UserLoginView, UserRegisterHelperView, ProfileDetailsView, \
    ProfileDeleteView, ChangeUserPasswordView, ProfileEditView, UserRegisterRefugeeView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    # path('register/staff/', UserRegisterStaffView.as_view(), name='register staff user'),
    path('register/helper/', UserRegisterHelperView.as_view(), name='register helper user'),
    path('register/refugee', UserRegisterRefugeeView.as_view(), name='register refugee user'),
    path('profile/delete/<int:pk>/', ProfileDeleteView.as_view(), name='profile delete'),
    path('profile/details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('profile/edit/<int:pk>', ProfileEditView.as_view(), name='profile edit'),
    path('edit-password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('index')), name='password_change_done'),
)