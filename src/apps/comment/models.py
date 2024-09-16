from django.db import models
from django.conf import settings
from apps.general.get_sentinel_user import get_sentinel_user


class DiscountComments(models.Model):
    """ Discount comments model """
    discount = models.ForeignKey('discount.Discount', on_delete=models.CASCADE, related_name='comments_discount')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user),
                             related_name='user_comments'
                             )
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Discount Comments'

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        if self.parent and self.parent.parent.parent is not None:
            raise ValueError('Comment can not have more than 2 levels of nested replies')
        super().save(*args, **kwargs)


