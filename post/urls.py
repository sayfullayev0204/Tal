from django.urls import path
from .views import video_list,news_list,news_detail,oav,tabrik,elon,email,tel,tel2,harid,tender,aksiya,arxiv

urlpatterns = [
    path('video-list/', video_list, name='video_list'),
    path('news_list/', news_list, name='news_list'),
    path('news_detail/<int:pk>', news_detail, name='news_detail'),  
    path('oav/', oav, name='oav'),
    path('tabrik/', tabrik, name='tabrik'),
    path('elon/', elon, name='elon'), 
    path('email/', email, name='email'),
    path('tel/', tel, name='tel'),
    path('tel2/', tel2, name='tel2'),
    path('harid/', harid, name='harid'),
    path('tender/', tender, name='tender'),
    path('aksiya/', aksiya, name='aksiya'), 
    path('arxiv/', arxiv, name='arxiv'),

]