from django.shortcuts import render,redirect

from django.views import View
from .models import Topic


from django.urls import reverse_lazy


class IndexView(View):

    def get(self, request, *args, **kwargs):

        topics  = Topic.objects.all()
        context = { "topics":topics }

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        posted  = Topic( comment = request.POST["comment"] )
        posted.save()

        #任意のページのパラメータにリダイレクトする。
        return redirect( request.build_absolute_uri(reverse_lazy("bbs:index")) + "?answer=true" )



index   = IndexView.as_view()
