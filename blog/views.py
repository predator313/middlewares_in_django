from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    print('hey i am a home view function')
    return HttpResponse('hey this is home page')
