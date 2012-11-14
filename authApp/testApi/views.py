from django.shortcuts import redirect, render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from tastypie.models import ApiKey

@login_required
def user_creds(request):
    loggedUser = request.user
    userApiKey = ApiKey.objects.get(user=request.user)
    redirectUrl = '/auth/?username=%s&api_key=%s&user=%s' % (loggedUser, userApiKey.key, loggedUser.pk)

    return redirect(redirectUrl)

@login_required
def auth_approved(request):
    return render_to_response('auth_approved.html', RequestContext(request))