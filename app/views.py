from django.shortcuts import render

# Create your views here.
def cond(request):
    dict={'a':1000,'b':300,'c':600}
    return render(request,'cond.html',dict)