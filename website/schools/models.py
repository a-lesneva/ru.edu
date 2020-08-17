from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=3)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'states'

class Suburb(models.Model):
    name = models.CharField(max_length=64)
    postcode = models.CharField(max_length=4)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'suburbs'

    def __str__(self):
        return f"{self.name} {self.state} {self.postcode}"

class School(models.Model):
    name = models.CharField(max_length=128)
    address_line = models.CharField(max_length=64)
    suburb = models.ForeignKey(Suburb, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    working_hours = models.CharField(max_length=64, blank=True)
    person = models.CharField(max_length=64, blank=True)
    details = models.TextField(blank=True)
    social_media = models.URLField(blank=True)
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'schools'

    def __str__(self):
        return f"{self.name}"