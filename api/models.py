from django.db import models

class Topic(models.Model):
    topic_text = models.CharField(max_length=255, blank=False, unique=True)
    userId = models.CharField(max_length=255, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.topic_text)
