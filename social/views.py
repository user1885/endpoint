from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, TemplateView
from django.urls import reverse

# Create your views here.

def redirect_to_index(request):
    return HttpResponseRedirect(reverse('social:index'))

class UserView(DetailView):
    template_name = 'social/user.html'
    context_object_name = 'target_user'
    queryset = get_user_model().objects.all()

    def get_object(self):
        user = self.queryset.filter(username=self.kwargs['username']).first()
        return user


class IndexView(TemplateView):
    template_name = 'social/index.html'
    