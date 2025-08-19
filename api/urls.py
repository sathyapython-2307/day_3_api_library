# ...existing code...
from rest_framework.routers import SimpleRouter
from .views import AuthorViewSet, BookViewSet
from django.urls import path, include

router = SimpleRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
