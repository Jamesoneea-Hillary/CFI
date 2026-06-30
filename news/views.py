from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import NewsPost, Category

def news_list(request):

    posts = NewsPost.objects.filter(
        published=True
    )

    categories = Category.objects.all()

    featured = posts.filter(featured=True).first()

    category_slug = request.GET.get("category")

    search = request.GET.get("search")

    if category_slug:

        posts = posts.filter(
            category__slug=category_slug
        )

    if search:

        posts = posts.filter(

            Q(title__icontains=search) |

            Q(excerpt__icontains=search)

        )

    # PAGINATION

    paginator = Paginator(posts, 6)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {

        "featured": featured,

        "posts": page_obj,

        "page_obj": page_obj,

        "categories": categories,

        "search": search,

    }

    return render(

        request,

        "news/news_list.html",

        context

    )


def news_detail(request, slug):

    post = get_object_or_404(

        NewsPost,

        slug=slug

    )

    post.views += 1

    post.save()

    related = NewsPost.objects.filter(

        category=post.category,

        published=True

    ).exclude(

        id=post.id

    )[:3]

    context = {

        "post": post,

        "related": related,

    }

    return render(

        request,

        "news/news_detail.html",

        context

    )