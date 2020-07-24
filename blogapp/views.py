from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from .forms import RegistrationForm,LoginForm,BlogCreateForm
from .models import Blog,Visitor
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login, logout



class UserRequiredMixing(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/login/')

        return super().dispatch(request, *args, **kwargs)

class HomeView(TemplateView):
	template_name='home.html'
    



class RegistrationView(CreateView):
    template_name='registration.html'
    form_class=RegistrationForm
    success_url = reverse_lazy('blogapp:login')	

    def form_valid(self,form):
        username=form.cleaned_data["username"]
        email=form.cleaned_data["email"]
        password=form.cleaned_data["password"]
        puja_user=User.objects.create_user(username=username,email=email,password=password)
        form.instance.user=puja_user
    	
        return super().form_valid(form)

class LoginView(FormView):
    template_name='login.html'
    form_class=LoginForm
    success_url = reverse_lazy('blogapp:home')	

    
    def form_valid(self, form):
        email=form.cleaned_data["email"]
        uname = form.cleaned_data["username"]
        pword = form.cleaned_data["password"]


        user = authenticate(email=email,username=uname, password=pword)

        if user is not None:
            login(self.request, user)
        else:
            return render(self.request, "login.html", {
                "form": form,
                "error": "Invalid username or password"
            })

        return super().form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')  


class ProfileView(UserRequiredMixing,TemplateView):
    template_name='profile.html'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logged_user = User.objects.get(username=self.request.user.username)
        visitor = Visitor.objects.get(user=logged_user) 
        context['visitor'] = visitor 

        return context      

class ProfileUpdateView(UserRequiredMixing,UpdateView):
    template_name = "registration.html"
    form_class = RegistrationForm
    model = Visitor
    success_url = reverse_lazy('blogapp:profile')


class BlogCreateView(LoginRequiredMixin, CreateView):
    form_class = BlogCreateForm
    template_name = 'blogcreate.html'
    success_url = reverse_lazy('blogapp:bloglist')


    def form_valid(self, form):
        if self.request.user.is_authenticated:
            visitor = self.request.user
            author=Visitor.objects.get(user=visitor)
            form.instance.author=author
            form.save()
            return redirect(self.success_url)






class BlogListView(UserRequiredMixing,ListView):
    template_name = 'bloglist.html'
    model = Blog
    context_object_name = 'blogs'

class BlogEditView(UpdateView):
    template_name = "blogcreate.html"
    form_class = BlogCreateForm
    model = Blog
    success_url = reverse_lazy('blogapp:bloglist')






  


