from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.template.loader import get_template
from django.views import generic
from django.core.signing import BadSignature, SignatureExpired, loads, dumps

from sns_majhong.forms import LoginForm, UserCreateForm, UserProfileUpdateForm

# app内でカスタムしたUserを使用する
User = get_user_model()


class UserCreate(generic.CreateView):
    template_name = 'register/user_create.html'
    form_class = UserCreateForm
    
    def form_valid(self, form):
        user =form.save(commit=False)
        user.is_active = False
        user.save()
        
        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': 'https' if self.request.is_secure() else 'http',
            'domain': domain,
            'token': dumps(user.pk),
            'user': user,
        }

        subject_template = get_template('register/mail_template/create/subject.txt')
        subject = subject_template.render(context)

        message_template = get_template('register/mail_template/create/message.txt')
        message = message_template.render(context)

        user.email_user(subject, message)
        return redirect('sns_majhong:user_create_done')


class UserCreateDone(generic.TemplateView):
    template_name = 'register/user_create_done.html'
    

class UserCreateComplete(generic.TemplateView):
    template_name = 'register/user_create_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60*60*24)
    
    def get(self, request, **kwargs):
        token = kwargs.get('token')
        try:
            user_pk = loads(token, max_age=self.timeout_seconds)

        except SignatureExpired:
            return HttpResponseBadRequest()
        
        except BadSignature:
            return HttpResponseBadRequest()
        
        else:
            try:
                user = User.objects.get(pk=user_pk)
            except User.DoesNotExist:
                return HttpResponseBadRequest()
            else:
                if not user.is_active:
                    user.is_active = True
                    user.save()
                    return super().get(request, **kwargs)
        
        return HttpResponseBadRequest()
                

class Index(generic.TemplateView):
    template_name = 'index.html'


class Login(LoginView):
    from_class = LoginForm
    template_name = 'login.html'


class Logout(LogoutView):
    template_name = 'index.html'


class RestrictLoginMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == int(self.kwargs['pk']) or user.is_superuser


class UserProfileUpdateView(RestrictLoginMixin, generic.UpdateView):
    model = User
    form_class = UserProfileUpdateForm
    template_name = 'profile.html'

    def get_success_url(self):
        return redirect('/sns_majhong/')