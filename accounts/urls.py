from django.urls import path
from accounts.views import SignupView, CustomTokenObtainPairView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import JobSeekerProfileViewSet, EmployerProfileViewSet

router = DefaultRouter()
router.register(r'jobseekers', JobSeekerProfileViewSet)
router.register(r'employers', EmployerProfileViewSet)

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='custom_login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
