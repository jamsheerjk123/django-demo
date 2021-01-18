from django.shortcuts import render ,HttpResponse,redirect
from .models import ProductModel
from requests import get
from youtube_dl import YoutubeDL
import json
from .forms import Product_Create_Form

# Create your views here.
def home (request):
    return render(request,'index.html')
def pro (request):
    
    products=ProductModel.objects.all()
    context={
        'products':products
    }
    return render(request,"table.html", context)
# def greet(request):
#     YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}

#     def search(arg):
#         with YoutubeDL(YDL_OPTIONS) as ydl:
#             try:
#                 get(arg) 
#             except:
#                 video = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
#             else:
#                 video = ydl.extract_info(arg, download=False)

#         return video

#     print(json.dumps(search('bombay dreams'), indent=2))
def create_product(request):
    if request.method=='POST':
        form=Product_Create_Form(request.POST)
        if form.is_valid():
            
            name=form.cleaned_data['name']
            price=form.cleaned_data['price']
            description=form.cleaned_data['description']
            product=ProductModel(name=name,price=price,description=description)
            product.save()
            return redirect('/main/table/')
        else:
            return render(request,'create_data.html',{'form':form} )   
    form=Product_Create_Form()
    return render(request,'create_data.html',{'form':form})      

        
    
   
    

    


    