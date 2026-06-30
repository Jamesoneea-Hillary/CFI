from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import news
from news.models import NewsPost
from donations.models import Donation
from contacts.models import ContactMessage
from django.contrib.auth.views import LoginView, LogoutView
from work.models import (
    WorkPage,
    ProgramArea,
    Project,
    ImpactMetric,
    SuccessStory
)

@login_required
def dashboard_home(request):
    context = {
        "news_count": NewsPost.objects.count(),
        "donations_count": Donation.objects.count(),
        "contacts_count": ContactMessage.objects.count(),

        "work_pages": WorkPage.objects.count(),
        "programs": ProgramArea.objects.count(),
        "projects": Project.objects.count(),
        "stories": SuccessStory.objects.count(),

        "latest_news": NewsPost.objects.order_by('-id')[:5],
        "latest_donations": Donation.objects.order_by('-id')[:5],
        "latest_contacts": ContactMessage.objects.order_by('-id')[:5],
    }
    return render(request, "dashboard/home.html", context)

def news_list(request):
    news = NewsPost.objects.all().order_by('-id')
    return render(request, 'dashboard/news_list.html', {'news': news})


# CREATE
def news_create(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image')

        news.objects.create(
            title=title,
            content=content,
            image=image
        )
        return redirect('news_list')

    return render(request, 'dashboard/news_form.html')


# EDIT
def news_edit(request, id):
    article = get_object_or_404(news, id=id)

    if request.method == "POST":
        article.title = request.POST['title']
        article.content = request.POST['content']

        if request.FILES.get('image'):
            article.image = request.FILES['image']

        article.save()
        return redirect('news_list')

    return render(request, 'dashboard/news_form.html', {'article': article})


# DELETE
def news_delete(request, id):
    article = get_object_or_404(news, id=id)
    article.delete()
    return redirect('news_list')

class DashboardLoginView(LoginView):
    template_name = "dashboard/login.html"
    redirect_authenticated_user = True


class DashboardLogoutView(LogoutView):
    next_page = "login"