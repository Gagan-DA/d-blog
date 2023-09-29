from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,FormView
from blog.models import Post,Category,Comment
from blog.forms import PostForm,UpdatePostForm,CommentForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect

# def home(request):
#     return render(request,'home.html',{})


def CategoryView(request,cname):
    category_posts=Post.objects.filter(category=cname)
    return render(request,'category.html',{'cname':cname.title(),'category_posts':category_posts})

def likeView(request,pk):
    post = get_object_or_404(Post,id=request.POST.get('post_id'));
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article',args=[str(pk)]))

class HomeView(ListView):
    model=Post 
    template_name='home.html' 
    # ordering=['-id']
    ordering=['-postdate']


class ArticleView(DetailView):
    model=Post 
    template_name='article.html' 
    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        context['form'] = CommentForm
        return context

class MyFormView(CreateView):
    model=Comment
    form_class = CommentForm
    success_url=reverse_lazy('home')


class AddPostView(CreateView):
    model=Post 
    template_name='addpost.html' 
    #fields="__all__"
    form_class=PostForm
    success_url=reverse_lazy('home')

class UpdatePostView(UpdateView):
    model=Post 
    template_name='updatepost.html' 
    form_class=UpdatePostForm
    success_url=reverse_lazy('home')

class DeletePostView(DeleteView):
    model=Post 
    template_name='deletepost.html'
    success_url=reverse_lazy('home')

