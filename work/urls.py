from django.urls import path

from .views import (
    work_page,
    program_detail
)

urlpatterns = [
    path('', work_page, name='work'),
    path('program/<slug:slug>/', program_detail, name='program_detail'),
]