from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('article', views.article, name='article'),
    path('article/<int:pk>', views.article_detail, name='article_detail'),
    path('reports', views.report_list, name='report_list'),
    path('report<int:pk>', views.report, name='report_detail'),
    path('note_list', views.list_note, name='note_list'),
    path('detail_note/<int:pk>', views.detail_note, name='detail_note'),
    path('list_phto', views.photo_list, name='photo_list'),
    path('detail_photo/<int:pk>', views.detail_photo, name='detail_photo'),
    path('search', views.search, name='search'),
    path('category/<str:slug>', views.category, name='category'),
    path('about', views.about, name='about'),
    path('contacat', views.contact_us, name='contact_us'),
    path('video/<int:pk>', views.video_detail, name='video_detail'),
    path('video', views.video_list, name='video_list'),
    path('submitted', views.submitted_list, name='submitted_list'),
    path('submitted/<int:pk>', views.submitted_detail, name='submitted_detail'),

]
