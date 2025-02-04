from django.urls import path, include
from . import views

app_name= 'photo'

urlpatterns = [
    path('', 
         views.IndexView.as_view(), 
         name='index'),
    
    path('post/',
         views.CreatePhotoView.as_view(),
         name='post'),
    
    path('post_done',
         views.PostSuccessView.as_view(),
         name = 'post_done'),
    
    path('photos/<int:category>',
         views.CategoryView.as_view(),
         name='photos_cat'),
    
    path('user-list/<int:user>',
         views.UserView.as_view(),
         name='user_list'),
    
    path('photo-detail/<int:pk>',
         views.PhotoDetailView.as_view(),
         name='photo_detail'),
    
    path('mypage/',
         views.MypageView.as_view(),
         name='mypage'),
    
    path('photo/delete/<int:pk>/',
         views.PhotoDeleteView.as_view(),
         name = 'photo_delete'),
    
]
