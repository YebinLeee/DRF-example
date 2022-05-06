
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('accounts/', include('accountApp.urls')),
    
    path('api-auth/', include('rest_framework.urls')),
    
    path('quiz/', include('quiz.urls')), # quiz앱의 url 연결
    
    path('board/', include('board.urls')) # board앱의 url 연결
]
