from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length = 264, unique = True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    name = models.CharField(max_length = 254, unique = True)
    url = models.URLField(unique = True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete = models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class USER(models.Model):
    firstName = models.CharField(max_length = 128)
    lastName = models.CharField(max_length = 128)
    email = models.EmailField(max_length = 254, unique = True)

    def __str__(self):
        return [self.firstName, self.lastName, self.email]
