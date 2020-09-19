from django.contrib import admin
from django.urls import include, path # includeを追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('techapp.urls')), # この行を追加
]
