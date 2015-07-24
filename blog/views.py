from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response,render, Http404
from django.core.context_processors import csrf
from django.http import HttpResponse
from blog.forms import *
from django.template import RequestContext, loader
from django.template.loader import get_template
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from blog.models import Post, Comment
from dev_pms.models import *
import time
##import calendar import month_name


def main(request):
    posts = Post.objects.order_by('-created')
    paginator = Paginator(posts, 2)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)
    return render_to_response('blog/list.html', RequestContext(request,{'posts':posts}))


def post(request, pk):
    post = Post.objects.get(pk=int(pk))
    comments = Comment.objects.filter(post=post)
    d = { 'post':post, 'comments':comments, 'form':CommentForm(),'user':user.request.user}
    d.update(csrf(request))
    return render_to_response('post.html', RequestContext(request, d))


def mkmonth_lst():
    if not Post.objects.count():
        return []
    year, month = timelocaltime()[:2]
    first = Post.objects.order_by('created')[0]
    fyear = first.created.year
    fmonth = first.created.month
    months = []
    for y in range(year,fyear-1, -1):
        start,end = 12,0
        if y == year:
            start=month
        elif y == fyear:
            end = fmonth-1
        for m in range(start, end, -1):
            months.append((y, m, month_name[m]))
    return months


def month(request, year, month):
    posts = Post.objects.filter(created__year=year, created__month=month)
    return render_to_response('blog/list.html', RequestContext(request, {'posts':posts, 'user':user.request.user,'post_list':posts.object_list,'months':mkmonth_lst()}))
        
