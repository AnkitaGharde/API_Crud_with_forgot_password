from django.shortcuts import render,redirect
from myapp.models import candidate
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import login
import random

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import candidateSerializer

# Create your views here.

def dashbord(request):
    return render(request,'myapp/dashbord.html')

def djangodash(request):
    return render(request,'myapp/django-dashboard.html')


def signup(request):

    if request.method=="POST":
        Firstname=request.POST['Firstname']
        Lastname=request.POST['Lastname']
        email = request.POST['email']

        mobile = request.POST['mobile']
        password = request.POST['password']
        candidate(Firstname=Firstname,Lastname=Lastname,email=email,mobile=mobile,password=password).save()



        messages.success(request,'The new user' +request.POST['Firstname']+"is  saved Successfully.... ")
        return render(request,'myapp/dashbord.html')
    else:
        return render(request,'myapp/signup.html')


def login(request):
    if request.method=="POST":
        try:
            Userdetails=candidate.objects.get(email=request.POST['email'],password=request.POST['password'])
            print("Firstname=",Userdetails)
            request.session['email']=Userdetails.email
            return render(request,'myapp/django-dashboard.html')
        except candidate.DoesNotExist as e:
             messages.success(request,'Firstname/ password Invalid..')


    return render(request,'myapp/login.html')


def logout(request):
    try:
        del request.session['email']
    except:
        return render(request,'myapp/dashbord.html')
    return render(request,'myapp/dashbord.html')


#-------------------------------------------------------
def resetpass(request):

    if request.method=="GET":

        return render(request,'myapp/resetpass.html')

    else:

        email=request.POST.get('email')

        request.session['em']=email

        query=candidate.objects.filter(email=email)

        if query:

            content = str(random.randint(100000,200000))

            request.session['OTP']=content

            send_mail('OTP',content,'ghardeankita6@gmail.com' , [email], fail_silently=False)

            return render(request,'myapp/reset_OTP.html')

        else:

            suc="your email is not Create"

            return render(request,'myapp/resetpass.html',{'suc':suc})



def OTP(request):

    otp=request.POST.get('OTP')

    ot=request.session['OTP']

    if ot==otp:

        return render(request,'myapp/forresetotp.html')

    else:

        suc="Your OPT is invalid"

        return render(request,'myapp/reset_OTP.html',{'suc':suc})

def passChange(request):

    pass1 = request.POST.get('password1')

    pass2 = request.POST.get('password2')

    if pass1 == pass2:

        email = request.session['em']

        a = candidate.objects.get(email=email)

        a.password = pass1

        a.save()

        suc = "Your Password is succesfully Change "

        return redirect('login')

    else:

        suc = "Your Conform password  is not match "

        return render(request, 'myapp/resetpass_snew.html', {'suc': suc})


#-------------------------------------------------------------------------------------------
#API section

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/user-list/',
		'Detail View':'/user-detail/<str:pk>/',
		'Create':'/user-create/',
		'Update':'/user-update/<str:pk>/',
		'Delete':'/user-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def userList(request):
	tasks = candidate.objects.all().order_by('-id')
	serializer = candidateSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def userDetail(request, pk):
	tasks = candidate.objects.get(id=pk)
	serializer = candidateSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def userCreate(request):
	serializer = candidateSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def userUpdate(request, pk):
	task = candidate.objects.get(id=pk)
	serializer = candidateSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def userDelete(request, pk):
	task = candidate.objects.get(id=pk)
	task.delete()

	return Response('User succsesfully deleted!')




