from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<div>hello  tourastic holidays is live</div>")
def packageinfo(request,package_name):
    return HttpResponse("<div>hello  tourastic holidays is live and we are on packageinfo page</div>")  
def contactpage(request):
    return HttpResponse("<div>hello  tourastic holidays is live and we are on contact us page</div>")  
def blogs(request):
    return HttpResponse("<div>hello  tourastic holidays is live and we are showing blogs </div>")      



