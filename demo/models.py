from django.db import models

class Building(models.Model):
    name    = models.CharField(max_length=50)
    slug	= models.SlugField(unique=True)
    location = models.ForeignKey('Location', null=True, blank=True)
    address	= models.CharField(max_length=100)
    description	= models.TextField(blank=True, default="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

    def __unicode__(self):
        return self.name

class Location(models.Model):
    name	= models.CharField(max_length=50)
    slug	= models.SlugField(max_length=50, unique=True)
    parent	= models.ForeignKey('self', null=True, blank=True, related_name='children')

    def __unicode__(self):
        return self.name

class BuildingImage(models.Model):
    building	= models.ForeignKey(Building, null=True, blank=True, related_name='images')
    image = models.FileField(upload_to="images/", blank=True)

    def __unicode__(self):
        return self.image.url
