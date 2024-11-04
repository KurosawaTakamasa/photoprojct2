from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    title = models.CharField(max_length=20, 
                             verbose_name='カテゴリ')
    
    def __str__(self):
        return self.title
    
    
class PhotoPost(models.Model):
    user = models.ForeignKey(CustomUser,
                             verbose_name='ユーザー',
                             on_delete=models.CASCADE)
    
    category = models.ForeignKey(Category,
                                 verbose_name='カテゴリ',
                                 on_delete=models.PROTECT)
    
    title = models.CharField(max_length=200,
                            verbose_name='タイトル')
    
    comment = models.TextField(verbose_name='コメント')
    
    image1 = models.ImageField(upload_to='photos',
                               verbose_name='イメージ1')
    
    image2 = models.ImageField(upload_to='photos',
                               verbose_name='イメージ2',
                               blank=True,
                               null=True)
    
    posted_at = models.DateTimeField(verbose_name='投稿日時',
                                     auto_now_add=True)
    
    def __str__(self):
        return self.title