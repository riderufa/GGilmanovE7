from board.views import AdvertList, AdvertDetail, AdvertStat, CreateTag, CreateComment, CreateAdvert, EditAdvert
from django.urls import path  
from django.views.decorators.cache import cache_page

app_name = 'board'  
urlpatterns = [  
    path('', AdvertList.as_view(), name='advert-list'),
    path('adverts/', AdvertList.as_view(), name='adverts-list'),  
    path('adverts/<int:pk>/', AdvertDetail.as_view(), name='advert-detail'),
    path('create/tag/', CreateTag.as_view(), name='create-tag'),  
    path('create/comment/', CreateComment.as_view(), name='create-comment'),
    path('create/advert/', CreateAdvert.as_view(), name='create-advert'),
    path('edit/advert/<int:pk>/', EditAdvert.as_view(), name='edit-advert'),
    path('stat/<int:pk>/', AdvertStat.as_view(), name='advert-stat'),
    
    # path('comments/', CommentList.as_view(), name='comment-list'),  
      
]