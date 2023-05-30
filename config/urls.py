from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('yangpt_app.urls')),
    path('login/', accounts.login, name='login'),
    path('logout/', accounts.logout, name='logout')
]
