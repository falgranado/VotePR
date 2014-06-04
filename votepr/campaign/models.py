from django.db import models

# Create your models here.

class Campaign(object):
	campaign_desc
	campaign_position
	campaign_email
	campaign_title

class CampaignParticipant(object):
	name
	email
	municipality
	zipcoode
	