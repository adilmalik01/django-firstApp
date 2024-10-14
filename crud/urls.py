"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf:
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, reverse
from django.contrib.auth import views as auth_views
from Home.views import RenderHome, About, Service, Contact, signup, profile, custom_logout_view, book_detail, book_delete, book_update
from django.http import HttpResponseRedirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RenderHome, name='home'),  
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('service/', Service, name='service'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  
    path('logout/', custom_logout_view, name='logout'),  
    path('accounts/login/', lambda request: HttpResponseRedirect(reverse('login'))),
    path('signup/', signup, name='signup'), 
    path('profile/', profile, name='profile'),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('book/<int:book_id>/update/', book_update, name='book_update'),
    path('book/<int:book_id>/delete/', book_delete, name='book_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
