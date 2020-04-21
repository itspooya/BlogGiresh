from . import views
from django.urls import path
from django.conf.urls import url


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),

    url(r'^representation/', views.Representation),
    url(r'^about/$', views.About),
    url(r'^govash/$', views.govash),
    url(r'^acleryc/$', views.acleryc),
    url(r'^catalog/$', views.catalog),
    url(r'^abouten/$',views.abouten),
    url(r'^indexen/',views.indexen),
    path('blog', views.BlogList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
