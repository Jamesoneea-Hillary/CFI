from django.db import models


class WorkPage(models.Model):

    title = models.CharField(max_length=255)

    subtitle = models.TextField()

    hero_image = models.ImageField(
        upload_to='work/hero/'
    )

    def __str__(self):
        return self.title


class ProgramArea(models.Model):

    title = models.CharField(max_length=200)

    slug = models.SlugField(
        unique=True
    )

    image = models.ImageField(
        upload_to='work/programs/'
    )

    short_description = models.TextField()

    description = models.TextField()

    def __str__(self):
        return self.title


class Project(models.Model):

    program = models.ForeignKey(
        ProgramArea,
        on_delete=models.CASCADE,
        related_name='projects'
    )

    title = models.CharField(max_length=255)

    image = models.ImageField(
        upload_to='work/projects/'
    )

    summary = models.TextField()

    content = models.TextField()

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title


class ImpactMetric(models.Model):

    title = models.CharField(max_length=200)

    value = models.CharField(max_length=100)

    icon = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return self.title


class SuccessStory(models.Model):

    title = models.CharField(max_length=255)

    beneficiary_name = models.CharField(
        max_length=255
    )

    image = models.ImageField(
        upload_to='work/stories/'
    )

    story = models.TextField()

    created_at = models.DateField()

    def __str__(self):
        return self.title