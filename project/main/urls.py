from django.urls import path

from project.main.views.generic import HomeView, ProvideHelpInfoView, RegisterAsView
from project.main.views.job import CreateJobView, EditJobView, DetailsJobView, AllJobView
from project.main.views.shelter import CreateShelterView, DeleteShelterView, EditShelterView, DetailsShelterView, \
    AllSheltersView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('provide/', ProvideHelpInfoView.as_view(), name='provide help info'),
    path('register/', RegisterAsView.as_view(), name='register as'),
    path('shelter/', AllSheltersView.as_view(), name='shelters'),
    path('shelter/create/', CreateShelterView.as_view(), name='create shelter'),
    path('shelter/delete/<int:pk>/', DeleteShelterView.as_view(), name='delete shelter'),
    path('shelter/edit/<int:pk>/', EditShelterView.as_view(), name='edit shelter'),
    path('shelter/details/<int:pk>/', DetailsShelterView.as_view(), name='details shelter'),

    path('job/', AllJobView.as_view(), name="jobs"),
    path('job/create/', CreateJobView.as_view(), name='create job'),
    path('job/edit/<int:pk>/', EditJobView.as_view(), name='edit job'),
    path('job/details/<int:pk>/', DetailsJobView.as_view(), name='details job'),
)