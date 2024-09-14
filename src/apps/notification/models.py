from django.db import models
import config.settings.auth



class Notification(models.Model):
    """ Notification model"""
    title = models.CharField(max_length=255)
    message = models.TextField(max_length=500)

    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name='notifications')
    branch = models.ForeignKey('branch.Branch', on_delete=models.SET_NULL, related_name='notifications',
                               blank=True, null=True)

    user = models.ForeignKey(config.settings.auth.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='notifications')

    created_at = models.DateTimeField(auto_now_add=True)