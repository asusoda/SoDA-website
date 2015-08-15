from django.db import models

# Create your models here.

class PostInfo(models.Model):

	title = models.CharField(unique=True,verbose_name="Title of post",max_length=100)

	date = models.DateField(verbose_name="Date of publication",auto_now_add=False)

	body = models.TextField(verbose_name="Text Body of the post")

	location = models.CharField(unique=False,verbose_name="Location of the annuncement",max_length=100, blank=True)
	
	card_image = models.ImageField(verbose_name="Image for mdl-card__media",blank=True)

	link_title = models.CharField(verbose_name="General Link name",max_length="100",blank=True,unique=False,default="")

	link_url = models.URLField(verbose_name="General URL for Link",blank=True,unique=False,default="")

	#Makes PostInfo Abstract 
	class Meta:
		abstract = True
	
	def __unicode__(self):
		return self.title

class Competition(PostInfo):
	
	#Different types of coding competitons 
	#Used to organize and query database in the view
	TYPE_OF_HACK = (
		('past hacks', 'Past Hackathons/Coding Competitions'),
		('upcoming hack','Future Hackathons/Coding Competitions'),
		)
	#Admin can pick what type of coding event 
	competition_type = models.CharField(max_length=50,choices=TYPE_OF_HACK,default='upcoming hacks')

	competition_website = models.CharField(verbose_name="Name of the Competition Website",max_length=100,blank=True,default="")

	competition_website_url = models.URLField(verbose_name="URL for Competition Website",blank=True,unique=False,default="")

	google_map = models.TextField(verbose_name="iframe for google map",blank=True,unique=False,default="")

	
	def __unicode__(self):
		return self.title

 
class Announcement(PostInfo):
	
	headline = models.BooleanField(default=False)

	def __unicode__(self):
		return self.title

class Project(PostInfo):
	
	git_name = models.CharField(max_length=100,verbose_name="Name of Github repo",blank=True,default="")

	git_link = models.URLField(verbose_name="Link to Github repo",blank=True)

	def __unicode__(self):
		return self.title

class Sponsor(models.Model):

	sponsor_name = models.CharField(max_length=100,verbose_name="Name of Sponsor")
	
	TIERS = (
		('Gold','Gold'),
		('Silver',"Silver"),
		('Bronze','Bronze'),
		)

	sponsorship_tier = models.CharField(max_length=100,verbose_name="Sponsorship Tier",choices=TIERS,default='Gold')

	vector_image = models.ImageField(verbose_name='Image of Company Logo')

	def __unicode__(self):
		return self.sponsor_name