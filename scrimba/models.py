from django.db import models


class Scream(models.Model):
    userHandle = models.CharField(max_length=120) # represents the user who submitted this
    body = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userHandle
    