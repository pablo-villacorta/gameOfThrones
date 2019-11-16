from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    related = models.ManyToManyField('self', symmetrical=False, related_name='related_to', through='Relationship')
    father = models.ForeignKey('Character', on_delete=models.SET_NULL, null=True, blank=True, related_name='_father')
    mother = models.ForeignKey('Character', on_delete=models.SET_NULL, null=True, blank=True, related_name='_mother')
    siblings = models.ManyToManyField('self', symmetrical=False, related_name='_siblings', through='Sibling')
    image = models.CharField(max_length=500, default='')
    house = models.ForeignKey('House', on_delete=models.SET_NULL, null=True, blank=True, related_name='characters_in_house')

    def __str__(self):
        return self.name

class House(models.Model):
    name = models.CharField(max_length=100)
    words = models.CharField(max_length=500, default='')
    logoURL = models.CharField(max_length=500, default='')
    allegiances = models.ManyToManyField('self', symmetrical=False, related_name='allegiance', through='Allegiance')
    def __str__(self):
        return self.name

class Sibling(models.Model):
    a = models.ForeignKey(Character, models.DO_NOTHING, related_name='a')
    b = models.ForeignKey(Character, models.DO_NOTHING, related_name='b') 

class Relationship(models.Model):
    from_person = models.ForeignKey(Character, models.DO_NOTHING, related_name='from_people')
    to_person = models.ForeignKey(Character, models.DO_NOTHING, related_name='to_people')

class Allegiance(models.Model):
    a = models.ForeignKey(House, models.DO_NOTHING, related_name='a')
    b = models.ForeignKey(House, models.DO_NOTHING, related_name='b')