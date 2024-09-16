from django.urls import path
from .views import *



urlpatterns = [
    path("create/", FeatureListCreateView.as_view(), name="feature_create"),
    path("feature/<int:pk>/", FeatureRetrieveUpdateDestroyView.as_view(), name="feature"),

    path("create/", FeatureValueListCreateView.as_view(), name="feature_value_create"),
    path("feature-value/<int:pk>/", FeatureValueRetrieveUpdateDestroyView.as_view(), name="feature_value"),

    path("create/", DiscountFeatureCombinationListCreateView.as_view(), name="feature_combination_create"),
    path("feature-combination/<int:pk>/", DiscountFeatureCombinationRetrieveUpdateDestroyView.as_view(),
                            name="discount_feature_combination"),

    path("create/", DiscountFeatureValueListCreateView.as_view(), name="discount_feature_create"),
    path("discount-feature/<int:pk>/", DiscountFeatureValueListCreateView.as_view(), name="discount_feature"),

]