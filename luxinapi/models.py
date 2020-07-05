from django.contrib.auth.models import User

class LuxinUser(User):

    class Meta:
        proxy = True
        ordering = ('firstname',)
