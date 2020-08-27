from rest_framework.routers import DefaultRouter
from api import views
from django.urls import path, include

router = DefaultRouter()
router.register('products', views.UserViewSet, basename='products-list')

urlpatterns =[
			path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    		path('auth/', include('rest_framework_social_oauth2.urls')),
    		path('register/', views.RegisterView.as_view(), name="register"),
    		path('email-verify/', views.VerifyEmail.as_view(), name="email-verify"),
    		path('login/', views.LoginAPIView.as_view(), name="login"),
    		path('request-reset-email/', views.RequestPasswordResetEmail.as_view(),name="request-reset-email"),
    		path('password-reset/<uidb64>/<token>/',views.PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    		path('password-reset-complete', views.SetNewPasswordAPIView.as_view(),name='password-reset-complete'),
]+router.urls