"""
URL configuration for Quiz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('users.urls')),
    path('',include('admin.urls'))
]


"""
{
    "refresh": 
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NTAwOTczOSwiaWF0IjoxNzQ0OTM3NzM5LCJqdGkiOiJmYTM2Y2Y2M2I0MWI0MDYxYWJkYWQ5MjU5MjRhYWNjOCIsInVzZXJfaWQiOjF9.YQMNuWK6-Ha61pn3GpZoBHafEJQ6fmGKS8eofTf-xOc",
    "access": 
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1MzY5NzM5LCJpYXQiOjE3NDQ5Mzc3MzksImp0aSI6IjVjM2IyOWI0NjliMTRkMDA5ZjFjOWFiNTEyMTQzMDYxIiwidXNlcl9pZCI6MX0.4z06dgy2oljDaf-TElMrNzzJptZKpWGXF9IdK_lPRIo"
}
"""