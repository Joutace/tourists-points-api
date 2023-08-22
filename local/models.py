"Native models lib import"
from django.db import models


class Local(models.Model):
    "Class representing a tourist point"
    name = models.CharField(max_length=150)
    description = models.TextField()
    working_period = models.TextField()
    min_age = models.IntegerField()

    def _str_(self):
        return self.name
