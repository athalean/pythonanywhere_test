from datetime import datetime, timedelta
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.template import Context, RequestContext
from django.utils.timezone import now
from panywhere.forms import CommentForm
from panywhere.models import Comment


def home(request):
    christmas = datetime(year=now().year, day=25, month=12, tzinfo=now().tzinfo)-now()
    if christmas < timedelta(0):
        christmas = datetime(year=now().year+1, day=25, month=12, tzinfo=now().tzinfo)-now()
    return render_to_response('home.html',
        RequestContext(request, {
        'comments': Comment.objects.all(),
        'now': now(),
        'christmas': christmas,
        'form': CommentForm()
    }))

def post(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if not form.is_valid():
            return render_to_response('post.html', RequestContext(request, {'form': form}))
        # make le comment here
        form.save()
        return redirect(reverse(viewname='home'))
    return render_to_response('post.html',
        RequestContext(request, {
        'form': CommentForm(request.POST if request.method == 'POST' else None)
    }))