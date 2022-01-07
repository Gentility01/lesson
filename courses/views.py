from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .forms import CourseModelForm
from .models import Courses

# Create your views here.


# def my_fbv(request, *args, **kwargs):
#     return render(request, 'about.html')

#BASE VIEW CLASS = VIEW
# tis handles the course view and the detail view
# class CourseView(View):
#     def get(self, request, id=None, *args, **kwargs):
#     #Get method
#         if id is not None:
#             obj = get_object_or_404(Courses, id=id)
#         context = {
#             'object':obj
#         }
#         return render(request, 'courses/course_detail.html', context)

#LISTVIEW
# class CourseListView(View):
#     def get(self, request, id=None, *args, **kwargs):
#         courselist = Courses.objects.all()
      
#         context = {
            
#             'object_list':courselist
#         }
#         return render(request, 'courses/course_list.html', context)


# class CourseCreateView(View):
#     def get(self, request, id=None, *args, **kwargs):
#        form = CourseModelForm()
#        context = {
#            'my_form':form
#        }
#        return render(request, 'courses/course_create.html', context)
    
#     def post(self, request, id=None, *args, **kwargs):
#         form = CourseModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = CourseModelForm()
#         context = {
#             'my_form':form
#         }
#         return render(request, 'courses/course_create.html', context)
       
    
    
# another way to to this 

class CourseCreateView(View):
    def get(self, request, id=None, *args, **kwargs):
       form = CourseModelForm()
       context = {
           'my_form':form
       }
       return render(request, 'courses/course_create.html', context)
    
    def post(self, request, id=None, *args, **kwargs):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {
            'my_form':form
        }
        return render(request, 'courses/course_create.html', context)
    
    
class CourseView(View):
    template_name = 'courses/course_detail.html'
    def get(self, request, id=None, *args, **kwargs):
        context={}
        if id is not None:
            obj = get_object_or_404(Courses, id=id)
            context['object'] = obj
        return render(request,self.template_name, context)
    
    
    
    
#update and detail together
class CourseUpdateView(View):
    template_name = 'courses/course_update.html' #update
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Courses, id=id)
        return obj
    
    def get(self, request, id=None, *args, **kwargs):
        #Get method
        context = {}
        obj =self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)
    
    def post(self, request, id=None, *args, **kwargs):
        #Post methoid
        context = {}
        obj = self.get_object()
        if obj is not None:
            form =CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)
    
    
class CourseDeleteView(View):
    template_name = 'courses/course_delete.html'
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Courses, id=id)
        return obj
    def get(self, request, id=None, *args, **kwargs):
        #Get method
        context = {}
        obj =self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
        return render(request, self.template_name, context)
    
    def post(self, request, id=None, *args, **kwargs):
        #Post methoid
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/list/')
        return render(request, self.template_name, context)
    
    
    
    
# list View
class CourseListView(View):
    template_name = 'courses/course_list.html'
    courselist = Courses.objects.all()
    
    def get_courselist(self):
        return self.courselist
    
    def get(self, request, *args, **kwargs):
        context = {
            'object_list':self.get_courselist()
        }
        return render(request,self.template_name, context)
    
#TO FILTER A PARTICULAR ID FROM LIST VIEW
# class CourseFilterView(CourseListView):
#     courselist = Courses.objects.filter(id=3)



    
    





    
