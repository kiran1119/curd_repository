from django.conf.urls import include, url
from django.contrib import admin
from curdapp import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'curdpro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.main_view),
    url(r'^create/', views.insert_view),
    url(r'^retrieve/', views.retrieve_view),
    url(r'^update/', views.update_view),
    url(r'^delete/', views.delete_view)
]
