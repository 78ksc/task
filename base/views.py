from django.shortcuts import render
# from django.http import HttpResponse
from .models import *
def index(request):
    jobPost = Job_post.objects.all()
    internPost = Intern_post.objects.all()
    changePost = X_post.objects.all()

    if request.method == 'POST':
        if 'job' in request.POST:
            j=request.POST['job']
            u=request.POST['user']
            user = User.objects.get(username = u)
            jins = Job_post.objects.get(id = j)
            print(u)
            print(user)
            # Japp.objects.create(user=user , job=jins )
            japp_in = Japp.objects.create(user=user, job=jins)
            print('job applied')
            return render(request,"summery.html",{'Japp':japp_in})

        if 'inte' in request.POST:
            j=request.POST['inte']
            u=request.POST['user']
            user = User.objects.get(username = u)
            jins = Intern_post.objects.get(id = j)
            japp_in = Iapp.objects.create(user=user , internship=jins )
            print('internship applied')
            return render(request,"summery.html",{'Japp':japp_in})



        if 'change' in request.POST:
            j=request.POST['change']
            u=request.POST['user']
            user = User.objects.get(username = u)
            jins = Intern_post.objects.get(id = j)
            japp_in = Xapp.objects.create(user=user , xchange=jins )
            print('change applied')
            return render(request,"summery.html",{'Japp':japp_in})



    context={
        'jPost':jobPost,
        'iPost':internPost,
        'xPost':changePost,
    }
    return render(request,"index.html",context)