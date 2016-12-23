from django.shortcuts import render
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
import json
# from hack_book.models import UserProfile
#
# # Create your views here.
# def user_check(request):
#     user = request.GET["id"]
#     password = request.GET["password"]
#
#     user_pw=list(UserProfile.objects.filter(user_id=user).values('user_pw'))
#     print(user, password, password==user_pw)
#     return HttpResponse(json.dumps(True), content_type='application/json')
#
# def login_user(request):
#     if request.method == "POST":
#         user_id = request.POST['user']
#     request.session['user_id'] = user_id
#
#     #user = authenticate(username=user_id, password=password)
#
#     return redirect(reverse_lazy('Index'))