from django.db import models
 
 
def _get_latest_post(queryset):
    """もらったクエリセットを、さらに絞り込んで返す。"""
 
    return queryset.filter(is_publick=True).order_by('-created_at')[:5]
 
 
class BigCategory(models.Model):
    """大カテゴリ"""
 
    name = models.CharField("大カテゴリ名", max_length=255)
    created_at = models.DateTimeField("作成日", auto_now_add=True)
 
    def __str__(self):
        return self.name
 
    def get_latest_post(self):
        queryset = Post.objects.filter(category__parent=self)
        return _get_latest_post(queryset)
 
 
class SmallCategory(models.Model):
    """小カテゴリー"""
 
    name = models.CharField("小カテゴリ名", max_length=255)
    parent = models.ForeignKey(BigCategory, verbose_name="大カテゴリ", on_delete=models.CASCADE)
    created_at = models.DateTimeField("作成日", auto_now_add=True)
 
    def __str__(self):
        return self.name
 
    def get_latest_post(self):
        queryset = Post.objects.filter(category=self)
        return _get_latest_post(queryset)
 
 
class Tag(models.Model):
    """タグ"""
 
    name = models.CharField("タグ名", max_length=255)
    created_at = models.DateTimeField("作成日", auto_now_add=True)
 
    def __str__(self):
        return self.name
 
    def get_latest_post(self):
        queryset = Post.objects.filter(tag=self)
        return _get_latest_post(queryset)
 
 
class Post(models.Model):
    """ブログのポスト"""
 
    title = models.CharField("タイトル", max_length=255)
    text = models.TextField("本文")
    category = models.ForeignKey(SmallCategory, verbose_name="カテゴリ", on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True, verbose_name="タグ")
    thumbnail = models.ImageField("サムネイル", upload_to='thumbnail/', blank=True)
    is_publick = models.BooleanField("公開可能か?", default=True)
    is_html = models.BooleanField("HTMLソースか?", default=False)
    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)
 
    def __str__(self):
        return self.title
