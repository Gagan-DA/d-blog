from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255,null=True)
    def __str__(self) :
        return self.category 
    def get_absolute_url(self):
        return reverse('article',args=(str(self.id)))  

class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio=models.TextField()
    userimage = models.ImageField(upload_to="media/users",blank=True,null=True)
    phoneNo = models.CharField(max_length=255,blank=True,null=True)
    website_url = models.CharField(max_length=255,blank=True,null=True)
    facebook_url = models.CharField(max_length=255,blank=True,null=True)
    instagram_url = models.CharField(max_length=255,blank=True,null=True)
    twiiter_url = models.CharField(max_length=255,blank=True,null=True)
    def __str__(self) :
        return str(self.user) 
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    # content = models.TextField()
    content = RichTextField(blank=True,null=True)
    postslug = AutoSlugField(populate_from='title',unique=True,default=None,null=False)
    postdate= models.DateField(auto_now_add=True)
    category=models.CharField(max_length=255,default="Education")
    likes=models.ManyToManyField(User,related_name="blog_posts")
    postimage = models.ImageField(upload_to="media/",blank=True,null=True)
    def __str__(self) :
        return self.title + '|' +str(self.author)
    def get_absolute_url(self):
        return reverse('article',args=(str(self.id)))

def total_likes(self):
    return self.likes.count()

class Comment(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    comment = models.TextField()
    postdate= models.DateField(auto_now_add=True)
           
 
    def __str__(self) :
        return self.post.title + ' - ' +self.first_name+" "+self.last_name
    class Meta:
        ordering = ('-id',)
        