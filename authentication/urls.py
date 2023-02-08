from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from . import views

urlpatterns = [
	#user views
	path('',views.UserList.as_view(),name='user-list'),
	path('<int:pk>/',views.UserDetail.as_view(),name='user-detail'),
	
	#login
	path('', include('rest_framework.urls')),
    
	#tokens
	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),	
	path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

