from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    content = models.CharField(max_length=600)
    datetime = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(blank=True, null=True)
    done_or_not = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")
