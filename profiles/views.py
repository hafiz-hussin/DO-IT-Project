from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from profiles.models import History, profile
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def infobar(request):
    return render(request, "quiz_home.html", {})

@login_required
def userProfile(request):
    # user = request.user
    # context = {'user': user}

    template = 'profile.html'
    hst = History.objects.all().registered()
    for h in hst:
        print(h)
    page = request.GET.get('page', 1)
    paginator = Paginator(hst, 10)
    try:
        histories = paginator.page(page)
    except PageNotAnInteger:
        histories = paginator.page(1)
    except EmptyPage:
        histories = paginator.page(paginator.num_pages)
    print(histories)
    context = {'histories': histories}
    return render(request, template, context)

@login_required
def history_list_view(request):
    hst = History.objects.all().registered()
    page = request.GET.get('page', 1)
    paginator = Paginator(hst, 10)
    try:
        histories = paginator.page(page)
    except PageNotAnInteger:
        histories = paginator.page(1)
    except EmptyPage:
        histories = paginator.page(paginator.num_pages)
    context = {'students': histories}
    return render(request, 'history_list.html', context)
