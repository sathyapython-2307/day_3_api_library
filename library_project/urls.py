# ...existing code...
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h2>Welcome to the Library Management API!</h2><p>Visit <a href="/api/authors/">Authors</a> or <a href="/api/books/">Books</a>.</p>')

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
