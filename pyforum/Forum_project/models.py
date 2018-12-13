from django.db import models

class Forum(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)


class Comment(models.Model):
    content = models.CharField(max_length=1000)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)



# Create your models here.
