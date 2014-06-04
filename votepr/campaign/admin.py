from django.contrib import admin

# Register your models here.

from .models import Campaign, CampaignParticipant

admin.site.register(Campaign)
admin.site.register(CampaignParticipant)
