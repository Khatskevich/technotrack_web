from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from loginsys.forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout


def MyUserRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/search/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], email = form.cleaned_data['email'], password = form.cleaned_data['password'])
            user.save()
            myUser = user.myuser
            myUser.nickName = form.cleaned_data['username']
            myUser.save()
            return HttpResponseRedirect('/search/')
        else:
            return render_to_response('registration.html', {'form': form}, context_instance=RequestContext(request))
    else:
        ''' '''
        form = RegistrationForm()
        context = {'form':form}
        return  render_to_response('registration.html',context, context_instance=RequestContext(request))

def LoginRequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/search/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            myUser = authenticate(username=username, password=password)
            if myUser is not None:
                login(request, myUser)
                return HttpResponseRedirect('/search/')
            else:
                return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
        else:
            return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
    else:
        ''' user is not submitting the form, show the login form '''
        form = LoginForm()
        context = {'form': form}
        return render_to_response('login.html', context, context_instance=RequestContext(request))


def LogoutRequest(request):
    logout(request)
    return HttpResponseRedirect('/')