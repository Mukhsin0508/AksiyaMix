from sys import maxsize
from django.db import models
from ..general.image_size import parent_category_image_size
from ..general.normalizer import normalizer_text


class Category(models.Model):
    """ Three levels of Categories model in parent.parent.parent subcategories """
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    image = models.ImageField(upload_to='category/images/%Y/%m/%d/', validators=[parent_category_image_size])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_children(self):
        return self.children.all()

    def get_parent(self):
        return self.parent

    def clean(self):
        try:
            if not self.pk and self.parent.parent.parent:
                raise ValueError("Only three levels of categories are allowed")
        except AttributeError:
            pass

    def get_normalize_fields(self):
        return ["title", "parent"]

    def save(self, *args, **kwargs):
        normalizer_text(self)
        super().save(*args, **kwargs)

