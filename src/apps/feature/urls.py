from django.urls import path
from .views import *



urlpatterns = [
    path("create/", CreateFutureAPIView.as_view(), name="feature_create"),
    path("retrieve/<int:pk>/", RetrieveFutureAPIView.as_view(), name="feature_retrieve"),
    path("update/<int:pk>/", UpdateFutureAPIView.as_view(), name="feature_update"),
    path("delete/<int:pk>/", DeleteFutureAPIView.as_view(), name="feature_delete"),

    path("create/", CreateFeatureValueAPIView.as_view(), name="feature_value_create"),
    path("retrieve/<int:pk>/", RetrieveFeatureValueAPIView.as_view(), name="feature_value_retrieve"),
    path("update/<int:pk>/", UpdateFeatureValueAPIView.as_view(), name="feature_value_update"),
    path("delete/<int:pk>/", DeleteFeatureValueAPIView.as_view(), name="feature_value_delete"),

    path("create/", CreateDiscountFeatureAPIView.as_view(), name="discount_feature_create"),
    path("retrieve/<int:pk>/", RetrieveDiscountFeatureAPIView.as_view(), name="discount_feature_retrieve"),
    path("update/<int:pk>/", UpdateDiscountFeatureAPIView.as_view(), name="discount_feature_update"),
    path("delete/<int:pk>/", DeleteDiscountFeatureAPIView.as_view(), name="discount_feature_delete"),

]