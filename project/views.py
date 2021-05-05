from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


from .models import Upload, UploadPrivate,Member
from .forms import MemberForm

from django_app.ai_backends import loadImage,ai_test

def index(request):
        return render(request,'index.html',{})




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'registration/register.html', context)

def logins(request):
    all_members = Member.objects.all
    return render(request,'Logins.html',{'all':all_members})

def join(request):
    if request.method=='POST':
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()

        return render(request,'join.html',{})

    else:
        return render(request, 'join.html', {})

def image_upload(request):
    if request.method == 'POST':
        image_file = request.FILES['image_file']
        image_type = request.POST['image_type']
        if settings.USE_S3:
            if image_type == 'private':
                upload = UploadPrivate(file=image_file)
            else:
                upload = Upload(file=image_file)
            upload.save()
            image_url = upload.file.url
            print(image_url)
            print(request.user.username)

        else:
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            image_url = fs.url(filename)


        vysledok=ai_test(image_url)
        if vysledok==1:
            vysledok="Negativny"
        elif vysledok==0:
            vysledok="Pozitivny"
        data = Member(username=request.user.username, link=image_url,pozitivita=vysledok)
        data.save()
        print(vysledok)
        return render(request, 'index.html', {
            'image_url': image_url
        })
    return render(request, 'index.html')