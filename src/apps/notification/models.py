from django.db import models
from django.core.exceptions import ValidationError
import config.settings.auth

class Notification(models.Model):
    """ Notification model"""
    company = models.ForeignKey('company.Company',
                                on_delete=models.CASCADE,
                                related_name='notifications',
                                blank=True,
                                null=True)
    branch = models.ForeignKey('branch.Branch',
                               on_delete=models.SET_NULL,
                               related_name='notifications',
                               blank=True,
                               null=True)
    title = models.CharField(max_length=255)
    message = models.TextField(max_length=500)
    user = models.ForeignKey(config.settings.auth.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='notifications')
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.company and not self.branch:
            raise ValidationError("Either company or branch must be provided.")
        if self.company and self.branch:
            raise ValidationError("Only one of company or branch should be provided.")

    def __str__(self):
        return self.title

    @staticmethod
    def create_notification(user, company=None, branch=None, title="New Follow", message="You have a new follower."):
        """ Create a new follower notification"""
        notification = Notification(
            user=user,
            company=company,
            branch=branch,
            title=title,
            message=message
        )
        notification.full_clean()
        notification.save()
