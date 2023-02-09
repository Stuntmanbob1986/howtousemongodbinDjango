from django.db import models

# example for a class based view


class Promise(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    made_on = models.DateField()

    def __str__(self):
        return self.title

