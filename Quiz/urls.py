
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('users.urls')),
    path('',include('admin.urls'))
]


# { User
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NTA1NDE4OSwiaWF0IjoxNzQ0OTgyMTg5LCJqdGkiOiI0ZDk4NDE0NTY4MjQ0MjY0YjI2MDg0M2QyMDg2MWU0YSIsInVzZXJfaWQiOjJ9.vzoxdHmHvUAGGmNDKCOrNbzKX1bQS2n-NHLdN6ranJA",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1NDE0MTg5LCJpYXQiOjE3NDQ5ODIxODksImp0aSI6IjIwZDQ0Y2JlM2YyOTQyODhiMmNlZDk4MjJjMjY4ODNlIiwidXNlcl9pZCI6Mn0.mzcwv44WKw2BmmmjfggHAPPuON5miG2sWYcwTtPR7tY"
# }

# { Admin
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NTA1NDI1NSwiaWF0IjoxNzQ0OTgyMjU1LCJqdGkiOiJjYTQyNTNlYTk1MWQ0ZjI1ODg4ODI5Nzg0ZjFkZTEzNCIsInVzZXJfaWQiOjF9.dihmf1198HvleimGh0TjSlDLWb6JXpEcriGm5_SzmeA",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1NDE0MjU1LCJpYXQiOjE3NDQ5ODIyNTUsImp0aSI6IjU5Y2ZlN2U0ZjVmMjQ2NDdiMTJiYTM2Y2ZjMWI0MGZmIiwidXNlcl9pZCI6MX0.1OwPyFTr2w_ms9W8_bWB4drpnSFNZolntw3SIuVrxP4"
# }