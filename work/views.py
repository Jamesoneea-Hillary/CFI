from django.shortcuts import render
from django.shortcuts import (
    render,
    get_object_or_404
)

from .models import (
    WorkPage,
    ProgramArea,
    Project,
    ImpactMetric,
    SuccessStory
)


def work_page(request):

    hero = WorkPage.objects.first()

    programs = ProgramArea.objects.all()

    projects = Project.objects.filter(
        is_active=True
    )

    metrics = ImpactMetric.objects.all()

    stories = SuccessStory.objects.all()

    context = {
        'hero': hero,
        'programs': programs,
        'projects': projects,
        'metrics': metrics,
        'stories': stories,
    }

    return render(
        request,
        'work/work.html',
        context
    )

def program_detail(request, slug):

    program = get_object_or_404(
        ProgramArea,
        slug=slug
    )

    projects = Project.objects.filter(
        program=program
    )

    context = {

        'program': program,

        'projects': projects,
    }

    return render(
        request,
        'work/program_detail.html',
        context
    )