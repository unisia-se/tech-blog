from django.urls import reverse_lazy
from django.db.models import Q
from django.views import generic
from .models import Post
#import concurrent.futures
#import multiprocessing
#from multiprocessing import Process
import logging
#import sys
 
class BaseListView(generic.ListView):
    paginate_by = 10 
    def base_queryset(self):
        queryset = Post.objects.filter(
            is_publick=True).order_by('-created_at')
        logging.getLogger('command').debug('ON View.py > BaseListView')
        return queryset
 
class PostIndexView(BaseListView):
    def get_queryset(self):
        queryset = self.base_queryset()
        keyword = self.request.GET.get("quick")
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword))
        logging.getLogger('command').debug('ON View.py > PostIndexView')
        return queryset

class CategoryView(BaseListView):
    def get_queryset(self):
        queryset = self.base_queryset()
        category = self.kwargs.get("small")
        if category:
            queryset = queryset.filter(category__name=category)
        else:
            category = self.kwargs.get("big")
            queryset = queryset.filter(category__parent__name=category)
        logging.getLogger('command').debug('ON View.py > CategoryView')
        return queryset
 
 
class TagView(BaseListView):
    def get_queryset(self):
        tag = self.kwargs["tag"]
        queryset = self.base_queryset().filter(tag__name=tag)
        logging.getLogger('command').debug('ON View.py > TagView')
        return queryset
 
class ProfileView(BaseListView):
    def get_queryset(self):
        queryset = self.base_queryset()
        return queryset

class ContactView(BaseListView):
    def get_queryset(self):
        queryset = self.base_queryset()
        return queryset

class PpolicyView(BaseListView):
    def get_queryset(self):
        queryset = self.base_queryset()
        return queryset

class PostDetailView(generic.DetailView):
    model = Post
    # 2018/08/16 add hama >>> 
    def get_object(self, queryset=None):
        post = super().get_object()
        # M00008 2021/11/03 mod hama >>>
        logging.getLogger('command').debug(post.category)
        # 小カテゴリー名にPaidContentが含まれていない場合は、公開中であれば表示。
        # 小カテゴリー名にPaidContentが含まれている場合はは、公開中かつ、ログイン承認済である場合のみ表示。
        # 上記以外は、404エラーを表示。
        if str(post.category) not in str("PaidContent") and post.is_publick:
            return post
        elif str(post.category) in str("PaidContent") and post.is_publick and self.request.user.is_authenticated:
            return post
        else:
            raise Http404
        # <<<
    # <<<

