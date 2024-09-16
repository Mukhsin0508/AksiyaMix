from django.urls import path
from .views import *



urlpatterns = [
    path("create/", FeatureListCreateView.as_view(), name="feature_create"),
    path("feature/<int:pk>/", FeatureRetrieveUpdateDestroyView.as_view(), name="feature"),

    path("create/", FeatureValueListCreateView.as_view(), name="feature_value_create"),
    path("feature-value/<int:pk>/", FeatureValueRetrieveUpdateDestroyView.as_view(), name="feature_value"),

    path("create/", DiscountFeatureListCreateView.as_view(), name="discount_feature_create"),
    path("discount-feature/<int:pk>/", DiscountFeatureRetrieveUpdateDestroyView.as_view(), name="discount_feature"),

]