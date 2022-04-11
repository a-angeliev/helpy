from django.views import generic as views

from project.main.models import Campaign


class AllCampaignView(views.ListView):
    template_name = "main/campaign/all_campaign.html"
    model = Campaign
    paginate_by = 3
