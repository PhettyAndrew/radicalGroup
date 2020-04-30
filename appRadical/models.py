from django.db import models


# Create your models here.
# Info
class Info(models.Model):
    companyName = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.companyName


class Subscribe(models.Model):
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.email


# Team
class Team(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    facebook_link = models.URLField()
    twitter_link = models.URLField()
    linkedIn_link = models.URLField()


# Spinner
BUILDING_TYPE = (
    ('Unknown', 'unknown'),
    ('House', 'house'),
    ('Office', 'office'),
)


# Building
class Building(models.Model):
    buildingCode = models.IntegerField()
    buildingType = models.CharField(choices=BUILDING_TYPE, default='unknown', max_length=10)
    buildingImage = models.ImageField()
    cost = models.IntegerField()
    description = models.TextField()
    size = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)

    def __int__(self):
        return self.buildingCode


# Building Components
class Components(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    rooms = models.IntegerField(null=True)
    bedrooms = models.IntegerField(null=True)
    stories = models.IntegerField(null=True)
    toilets = models.IntegerField(null=True)
    kitchen = models.IntegerField(null=True)
    store = models.IntegerField(null=True)
    parkingSpace = models.IntegerField(null=True)
    additional_features = models.TextField(null=True)

    def __str__(self):
        return self.rooms


# Building plan
class Plan(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    planName = models.CharField(max_length=15)
    site_planImage = models.ImageField()
    floor_planImage = models.ImageField(null=True)
    cross_sectionImage = models.ImageField(null=True)
    external_elevationImage = models.ImageField(null=True)
    internal_elevationImage = models.ImageField(null=True)
    electrical_drawingImage = models.ImageField(null=True)
    plumbing_drawingImage = models.ImageField(null=True)
    landscape_planImage = models.ImageField(null=True)
    description = models.TextField()

    def __str__(self):
        return self.planName
