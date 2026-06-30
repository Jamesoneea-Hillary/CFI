from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):

    name = models.CharField(max_length=100)

    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class NewsPost(models.Model):

    title = models.CharField(max_length=255)

    slug = models.SlugField(unique=True, blank=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="posts"
    )

    featured_image = models.ImageField(
        upload_to="news/"
    )

    excerpt = models.TextField()

    content = CKEditor5Field(
        "Content",
        config_name="default"
    )

    author = models.CharField(
        max_length=120,
        default="Community Focus International"
    )

    featured = models.BooleanField(default=False)

    published = models.BooleanField(default=True)

    views = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title