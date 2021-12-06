
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('country',views.country_fun,name='country'),
    path('',views.showcountry,name='homepage'),
    path('page2index',views.index_pass_name,name='page2index'),
    path('webpage1',views.webpage1,name='webpage1'),
    path('webpage2',views.webpage2,name='webpage2'),
]
