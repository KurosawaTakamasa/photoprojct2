from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreatinForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = CustomUserCreatinForm
    template_name = 'signup.html'
    success_url = reverse_lazy('accounts:signup_success')
    
    #フォームに入力された情報を登録する処理
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class SignUpSuccessView(TemplateView):
    template_name = 'signup_success.html'