from django.db import models

# Create your models here.


class Campaign(models.Model):
    campaign_desc = models.TextField()
    campaign_position = models.CharField(max_length=10)  # for or against
    campaign_email = models.TextField()
    campaign_title = models.CharField(max_length=150)
    campaign_created_date = models.DateField()
    campaign_end_date = models.DateField()


class CampaignParticipant(models.Model):
    name = models.CharField(max_length=45)
    campaign = models.ForeignKey('Campaign')
    email = models.CharField(max_length=50)
    municipality = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
