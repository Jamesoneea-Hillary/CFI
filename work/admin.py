from django.contrib import admin

from .models import (
    WorkPage,
    ProgramArea,
    Project,
    ImpactMetric,
    SuccessStory
)


@admin.register(WorkPage)
class WorkPageAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(ProgramArea)
class ProgramAreaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'program',
        'is_active'
    )

    list_filter = (
        'program',
        'is_active'
    )


@admin.register(ImpactMetric)
class ImpactMetricAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'value'
    )


@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'beneficiary_name',
        'created_at'
    )