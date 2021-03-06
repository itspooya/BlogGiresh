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
    url(r'^catalog_en',views.catalogen),
    url(r'^aclerycen',views.Acrelycen),
    url(r'^gouacheen',views.Govashen),
    url(r"^govashen",views.Govashen),
    url(r"^standard",views.standard),
    url(r"^en_standard",views.en_standard),
    url(r"^archive",views.Archive),
    path('blog', views.BlogList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
