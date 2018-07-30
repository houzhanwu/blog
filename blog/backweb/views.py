from django.shortcuts import render_to_response
from django.views.generic.base import View


class Login(View):
    def get(self, *args, **kwargs):
        return render_to_response('backweb/login.html')
