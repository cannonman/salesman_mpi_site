from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from salesman import views as salesman_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', salesman_views.index, name = 'index'),
    path('admin/', admin.site.urls, name = 'admin'),
    path('register/', salesman_views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'salesman/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'salesman/logout.html'), name = 'logout'),

    path('test/', salesman_views.test, name = 'test'),
    path('new/', salesman_views.new_file, name = 'new'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

