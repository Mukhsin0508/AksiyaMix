"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .yasg import schema_view
from debug_toolbar.toolbar import debug_toolbar_urls

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path("admin/", admin.site.urls),

    # ================== API URLS ====================
    # path("api/v1/ads/", include("apps.ads.urls")),
    # path("api/v1/auth/", include("apps.authentication.urls")),
    # path("api/v1/branch/", include("apps.branch.urls")),
    # path("api/v1/category/", include("apps.category.urls")),
    # path("api/v1/comment/", include("apps.comment.urls")),
    path("api/v1/company/", include("apps.company.urls")),
    # path("api/v1/complaint/", include("apps.complaint.urls")),
    path("api/v1/discount/", include("apps.discount.urls")),
    path("api/v1/feature/", include("apps.feature.urls")),
    # the general app is left out because it's unnecessary for APIs
    # path("api/v1/notification/", include("apps.notification.urls")),
    # path("api/v1/owner/", include("apps.owner.urls")),
    # path("api/v1/payment/", include("apps.payment.urls")),
    # path("api/v1/review/", include("apps.review.urls")),
    # path("api/v1/search/", include("apps.search.urls")), # do we need this?
    path("api/v1/user/", include("apps.user.urls")),
    # path("api/v1/wishlist/", include("apps.wishlist.urls")),

    # ==================== Swagger and Redoc ====================
    path ( '' , schema_view.with_ui ( 'swagger' , cache_timeout=0 ) , name='schema-swagger-ui' ) ,
    path ( 'redoc/' , schema_view.with_ui ( 'redoc' , cache_timeout=0 ) , name='schema-redoc' ),

    # ==================== CKEditor ====================
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # ==================== Simple JWT ====================
    path ( 'api/token/' , TokenObtainPairView.as_view ( ) , name = 'token_obtain_pair' ) ,
    path ( 'api/token/refresh/' , TokenRefreshView.as_view ( ) , name = 'token_refresh' ) ,


] + debug_toolbar_urls()
