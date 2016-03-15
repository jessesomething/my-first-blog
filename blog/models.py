from django.db import models
from django.utils import timezone

# Creates an object class for each blog post
# to be used in a django database
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    # Publish method to get current timestamp and save it
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # Returns the title string of the post
    def __str__(self):
        return self.title
