from django.urls import path
from .views import OrganizationAPIView,OrganizationDetailsBy_ID

urlpatterns = [
    path('orgdata/',OrganizationAPIView.as_view()),
    path('dataid/<int:id>/',OrganizationDetailsBy_ID.as_view()),
]
