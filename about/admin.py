from django.contrib import admin
from .models import (
    AboutPage,
    VisionMission,
    CoreValue,
    Founder,
    BoardMember,
    Advisor,
    TeamMember
)

admin.site.register(AboutPage)
admin.site.register(VisionMission)
admin.site.register(CoreValue)
admin.site.register(Founder)
admin.site.register(BoardMember)
admin.site.register(Advisor)
admin.site.register(TeamMember)