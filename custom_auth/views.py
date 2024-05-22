from django.contrib.auth import get_user_model, login
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy, reverse
from . import forms

# Create your views here.

class IndexView(TemplateView):
    template_name = 'custom_auth/index.html'
    
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('social:index'))
        return super().get(request)


class SignUpView(FormView):
    template_name = 'custom_auth/sign_up_form.html'
    form_class = forms.SignUpForm
    success_url = reverse_lazy('social:index')
    
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('social:index'))
        return super().get(request)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(self.request, user)
        return super().form_valid(form)
    

class SignInView(FormView):
    template_name = 'custom_auth/sign_in_form.html'
    form_class = forms.SignInForm
    success_url = reverse_lazy('social:index')

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('social:index'))
        return super().get(request)

    def form_valid(self, form):
        username_or_email = form.cleaned_data['username_or_email'] 
        password = form.cleaned_data['password']
        user = get_user_model().objects.filter(username=username_or_email).first()
        if user is None:
            user = get_user_model().objects.filter(email=username_or_email).first()

        if user is None or not user.check_password(password):
            return super().get(self.request, error_message='Wrong username or password.')
        
        login(self.request, user)
        return super().form_valid(form)
