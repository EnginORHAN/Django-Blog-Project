from django.db import models

# Create your models here.

#model tablosu oluşturmak için 
#python manage.py makemigrations
#python manage.py migrate
#SQL database içerisine tablooluşturur

class Blog(models.Model):
    title = models.CharField(("Başlık"), max_length=50)
    text = models.TextField()
    date_now= models.DateTimeField(("Tarih - Saat"), auto_now=False, auto_now_add=False)
    author = models.CharField(("Yazar"), max_length=50)
    # null değerler none değer gönderir
    # default başlangıç değeri gönder
    # blank=true doldurulması zorunlu değil
    subtitle = models.CharField(("Alt Başlık"), max_length=50, default="",null=True,blank=True)
    isactive = models.BooleanField(("Sayfada Göster"),default=False)
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, verbose_name=("blog"), on_delete=models.CASCADE,null=True)
    fullname = models.CharField(("Ad - Soyad"), max_length=50,null=True)
    text = models.TextField(("Yorum"))
    date_now = models.DateTimeField(("Tarih - Saat"), auto_now = False, auto_now_add = True)
    


class Contact(models.Model):
    fullname=models.CharField(("Ad Soyad"), max_length=50)
    title = models.CharField(("Konu"), max_length=50)
    email = models.EmailField(("email"), max_length=254)
    text = models.TextField(("İletişim Mesajı"))
    
class Deneme(models.Model):
    baslik=models.CharField(("Başlık Deneme"), max_length=50)