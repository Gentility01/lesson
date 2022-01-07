from django.shortcuts import get_object_or_404, render
from django.urls import reverse
# from django.views.generic.edit import DeleteView
from .forms import ArticleModelForm
from .models import Article
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    UpdateView,
)
# Create your views here.

# def article_list(request):
#     form = Article.objects.all()
#     context = {
#         'my_form':form
    
        
#     }
#     return render(request, 'blog/article_list.html', context)



class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'   # here acording to the format the classbase view models has to be the the same name with the template store in the folder with the app name eg blog/modelname_list.html
    form_class = ArticleModelForm 
    queryset  = Article.objects.all()
    # success_url = 'article_list'
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    # this part overrides the detail page
    # def get_success_url(self):
    #     return '/'
    
    
class ArticleListView(ListView):
    template_name = 'blog/article_list.html'   # here acording to the format the classbase view models has to be the the same name with the template store in the folder with the app name eg blog/modelname_list.html 
    queryset  = Article.objects.all()
    
    
class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'   # here acording to the format the classbase view models has to be the the same name with the template store in the folder with the app name eg blog/modelname_list.html 
    queryset  = Article.objects.all()
    # to overwrite the pk to id in the urls
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)
    
    
class ArticleUpdateView(UpdateView):
    template_name = 'blog/article_create.html'   # here acording to the format the classbase view models has to be the the same name with the template store in the folder with the app name eg blog/modelname_list.html
    form_class = ArticleModelForm 
    queryset  = Article.objects.all()
    # success_url = '/'
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
     # to overwrite the pk to id in the urls
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)
    
    
    
class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'   # here acording to the format the classbase view models has to be the the same name with the template store in the folder with the app name eg blog/modelname_list.html 
    # queryset  = Article.objects.all()
    # to overwrite the pk to id in the urls
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)
    
    def get_success_url(self):
        return reverse('articles:article_list') # the article is the name of the app(app_name = articles) in the urls the article_list is the name of the path we want it to go to 
    



    