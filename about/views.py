from django.shortcuts import render
from .models import (
    AboutPage,
    VisionMission,
    CoreValue,
    Founder,
    BoardMember,
    Advisor,
    TeamMember
)

def about_page(request):

    about = AboutPage.objects.first()
    vm = VisionMission.objects.first()

    values = CoreValue.objects.all()
    founder = Founder.objects.first()

    board_members = BoardMember.objects.all()
    advisors = Advisor.objects.all()
    team_members = TeamMember.objects.all()

    context = {
        'about': about,
        'vm': vm,
        'values': values,
        'founder': founder,
        'board_members': board_members,
        'advisors': advisors,
        'team_members': team_members,
    }

    return render(request, 'about/about.html', context)