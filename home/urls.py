from .views import CategoryViewSet, IdeasViewSet, XizmatlarViewSet, TeamViewSet, CommitesViewSet, CompanyViewSet, ArticlesViewSet, UserLoginViewSet, MessageViewSet
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


schema_view = get_schema_view(
    openapi.Info(
        title="Payment API",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'ideas', IdeasViewSet, basename='ideas')
router.register('teams', TeamViewSet, basename='teams')
router.register('commites', CommitesViewSet, basename='commites')
router.register('company', CompanyViewSet, basename='company')
router.register('articles', ArticlesViewSet, basename='articles')
router.register('userlogin', UserLoginViewSet, basename='userlogin')
router.register('xizmatlar', XizmatlarViewSet, basename='xizmatlar')
router.register('messages', MessageViewSet, basename='messages')


urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', login_required(schema_view.with_ui('swagger', cache_timeout=0)), name='schema-swagger-ui'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]


urlpatterns += [
    re_path(r'swagger(?P<format>\.json|\.yaml)S', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
