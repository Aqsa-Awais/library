from django.db import models

class cabinets(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class racks(models.Model):
    name = models.CharField(max_length=200)
    cabinet = models.ForeignKey(cabinets, on_delete=models.CASCADE)

    def __str__ (self):
        return self.name

class books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    rack = models.ForeignKey(racks, on_delete=models.CASCADE)


    def __str__ (self):
        return self.title