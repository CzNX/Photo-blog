from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import My_Blog
from .forms import ModelForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):  # list of all
    obj = My_Blog.objects.all()
    paginator = Paginator(obj, 6)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {
        'obj': obj,
        'contacts': contacts,
    }
    return render(request, 'blog/index.html', context)


def detail(request, id):  # Retrieve
    obj = get_object_or_404(My_Blog, id=id)
    latest = My_Blog.objects.order_by('-date_time')[0:4]
    context = {
        'obj': obj,
        'latest': latest,
    }
    return render(request, 'blog/detail.html', context)


def create(request):  # create
    if request.method == 'POST':
        form = ModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post created successfully !')
            return redirect('/')
    else:
        form = ModelForm()

    context = {
        'form': form,
    }
    return render(request, 'blog/create.html', context,)


def update(request, id):  # update/Edit
    obj = get_object_or_404(My_Blog, id=id)
    form = ModelForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Profile updated successfully !')
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'blog/update.html', context)

@login_required(login_url='/admin')
def delete(request, id):  # delete post
    obj = get_object_or_404(My_Blog, id=id)
    obj.delete()
    messages.success(request, 'Post deleted successfully !')
    return redirect('/')

