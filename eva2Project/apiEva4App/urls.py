from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, ClienteViewSet, LibroViewSet

router = DefaultRouter()
router.register(r'autores', AutorViewSet, basename='autor')
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'libros', LibroViewSet, basename='libro')

urlpatterns = router.urls
