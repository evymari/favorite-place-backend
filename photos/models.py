from django.db import models

# Create your models here.
"""from django.db import models
from django.core.exceptions import ValidationError
from users.models import Child
from django.contrib.auth.models import User



class Event(models.Model):
    title = models.CharField(max_length=80, null=False)
    description = models.TextField()
    date = models.DateField()
    spots = models.IntegerField(default=0)


    def clean(self):
        if self.spots > 3:
            raise ValidationError("El número máximo de plazas es 3.")

    def __str__(self):
        return self.title


class EventRegistration(models.Model):
    event = models.ForeignKey(Event, related_name='registrations', on_delete=models.CASCADE)
    child = models.ForeignKey(Child, related_name='registrations', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='registrations', on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.child.first_name} - {self.event.title}"
"""