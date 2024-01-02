from django.shortcuts import render
from appMy.models import *
# Create your views here.

def indexPage(request):
    blog_list = Blog.objects.all()
    context={
        "blog_list":blog_list,
    }
    return render(request,"index.html",context)

def categoryPage(request, slug=None):
    
    if slug:
        blog_list = Blog.objects.filter(category__slug=slug)
    else:
        blog_list = Blog.objects.all()
        
    category_list = Category.objects.all()
    
    context={
        "blog_list":blog_list,
        "category_list":category_list,
    }
    return render(request,"category.html",context)

def aboutPage(request):
    blog_list = Blog.objects.all() #all liste mantığında çalışır [1.blog,2.blog,3.blog]
    blog_isactive = Blog.objects.filter(isactive=True) #[]liste mantığıyla çalışır buda
    blog2 = Blog.objects.get(id=2) # tek eleman çekmek için kullanılır sadece 2.objeyi çeker eğer çekilen blog yoksa filter ve all hata döndurmez ama get döndürür.
    denemeler=Deneme.objects.all()

    context={
        "blog_list":blog_list,
        "blog_isactive":blog_isactive,
        "blog2":blog2,
        "denemeler":denemeler
    }
    return render(request,"about.html",context)

#deneme detay start
def denemPage(request,slug):
    deneme=Deneme.objects.get(baslik=slug)
    context={
        "deneme":deneme,
    }
    return render(request,"deneme.html",context)
#deneme detay end

def contactPage(request):
    
    if request.method =="POST":
        fullname = request.POST.get("fullname")
        title = request.POST.get("title")
        email = request.POST.get("email")
        text = request.POST.get("text")
        
        contact = Contact(fullname = fullname, title=title,email=email,text=text) #obje oluşturuldu değişkene gönderildi
        contact.save() #değişken SQL DATABASE kaydedildi
    context={}
    return render(request,"contact.html",context)

def detailPage(request,bid):
    #kullanıcı yada frontend den bilgi almanın 2 yolu vardır
    #1- url adresi
    #2- formlardan
    print(bid)
    blog= Blog.objects.get(id=bid)
    
    comment_list=Comment.objects.filter(blog=blog)
    
    if request.method=="POST":
        fullname=request.POST.get("fullname")
        text=request.POST.get("comment") 

        if fullname and text:
            comment=Comment.objects.create(fullname=fullname, text=text,blog=blog)
            comment.save()
    
    context={
        "blog":blog,
        "comment_list":comment_list,
    }
    return render(request,"detail.html",context)

