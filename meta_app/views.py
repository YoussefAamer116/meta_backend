from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# # Create your views here.
# def home(request):
#     return HttpResponse("<html><body><h1>welcome to meta app</h1></body></html>")

# def dateoftoday(request):
#     date_time = datetime.today()
#     return HttpResponse(date_time)

# def index(request): 
#     path = request.path 
#     method = request.method 
#     content=''' 
# <center><h2>Testing Django Request Response Objects</h2> 
# <p>Request path : " {}</p> 
# <p>Request Method :{}</p></center> 
# '''.format(path, method) 
#     return HttpResponse(content) 

# def appname(request,app):
#     apps = {
#         'Facebook':'This is facebook',
#         'Instagram':'This is instagram',
#         'Whatsapp':'This is whatsapp',
#     }
#     description = apps[app]
#     return HttpResponse(f"<h1> {app} </h1>" + description)

# from .forms import InputForm
# def form_view(request):
#     form = InputForm()
#     context = {'form': form}
#     return render(request,'home.html',context)

# from .forms import LogForm
# def form_view(request):
#     form = LogForm()
#     if request.method=='POST':
#         form = LogForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {"form" : form}
#     return render(request,'home.html',context)

# def index(request):
    
#     context = {'user' : 'admin'}
#     return render(request, "index.html", context)
    
# def menu(request):
#     menuitem = {
#         'pricechart':[
#             {'name':'falafel', 'price':'12'}
#         ]
#     }
#     return render(request,"index.html",menuitem)