from django.shortcuts import render, render_to_response
from django.views.generic.base import View


class Index(View):
    def get(self, *args, **kwargs):
        return render_to_response('web/index.html')
