from django.shortcuts import render
from blog.models import Post
from shop.models import Item


def index(request):
    pl = Post.objects.all().order_by('-created_at')[0:3]
    il = Item.objects.all().order_by('-price')[:3]
    return render(request, 'main/index.html',
                {'post_list': pl, 'item_list':il})
