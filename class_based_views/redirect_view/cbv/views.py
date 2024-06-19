from typing import Any
from django.views.generic.base import TemplateView, RedirectView
from cbv.models import Post
from django.shortcuts import get_object_or_404
from django.db.models import F #?? F expression

class Ex2View(TemplateView):
    
    template_name = "ex2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.get(id=1)
        context["data"] = "Context data for Ex2"
        return context

class PostPreLoadTaskView(RedirectView):
    """
    This executes some stuff before the redirect is done.
    """

    # url = "http://arstechnica.com"
    pattern_name = 'cbv:singlepost'
    # permanent = True/False (301/302, default is False)

    def get_redirect_url(self, *args: Any, **kwargs: Any) -> str | None:
        """
        We override the method that does the redirect.
        We first execute a database update before it gives the redirect url.
        """

        # less efficient
        # post = get_object_or_404(Post, pk=kwargs['pk'])
        # post.count = F('count') + 1
        # post.save()

        post = Post.objects.filter(pk=kwargs['pk'])
        post.update(count=F('count') + 1) # voor update is geen save nodig

        return super().get_redirect_url(*args, **kwargs)


class SinglePostView(TemplateView):
    # NotImplemented # handy!!!

    template_name = "ex4.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        """
        We get the context data (a dict) and add a another item to it.
        """
        context = super().get_context_data(**kwargs)
        context["posts"] = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        
        return context