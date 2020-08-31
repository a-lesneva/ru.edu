from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=3)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'states'

class Suburb(models.Model):
    name = models.CharField(max_length=64)
    postcode = models.CharField(max_length=4)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)

    class Meta:
        managed = True
        db_table = 'suburbs'

    def __str__(self):
        return f"{self.name} {self.state} {self.postcode}"

class School(models.Model):
    name = models.CharField(max_length=200)
    address_line = models.CharField(max_length=64)
    suburb = models.ForeignKey(Suburb, on_delete=models.CASCADE, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    working_hours = models.CharField(max_length=64, blank=True)
    person = models.CharField(max_length=64, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    social_media = models.URLField(blank=True, null=True)
    active = models.BooleanField(default=True)
    google_map_link = models.URLField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'schools'

    def __str__(self):
        return f"{self.name}"
