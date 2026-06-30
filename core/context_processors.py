from contacts.models import ContactInfo
from work.models import ProgramArea


def site_data(request):
    return {
        "contact_info": ContactInfo.objects.first(),
        "footer_programs": ProgramArea.objects.all()[:6],
    }