from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('polls.urls')),  # เชื่อมต่อกับแอป polls
    # path('admin/', admin.site.urls),  # ใช้งาน Django Admin
]
