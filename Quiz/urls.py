
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('users.urls')),
    path('',include('adminz.urls'))
]


# { User
# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NTI4OTYxNywiaWF0IjoxNzQ1MjE3NjE3LCJqdGkiOiI1MmMwNWJmNTc0ZmY0MzBjYjhlZGY3ZWNlMDk2NGEzOSIsInVzZXJfaWQiOjR9.UfKKxWFSaVWK3ofsMuwhh9ZrlpdX5zevukbptD1AFOE",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1NjQ5NjE3LCJpYXQiOjE3NDUyMTc2MTcsImp0aSI6IjI3YTM4YTAwZjkyYTQ5ZTRiZGNmOWIyNzk0ZTU4ZDUzIiwidXNlcl9pZCI6NH0.A0tMW4Fwm1Aq0Ql57VZEsP9ftWpeFUBgXTXeC9JgIiY"
# }
# { Admin
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NTI5MDQ4MiwiaWF0IjoxNzQ1MjE4NDgyLCJqdGkiOiJmYmViYzNlZDVlY2M0OWJhODEzNzYwMWM4NTYxZWZjYiIsInVzZXJfaWQiOjV9.6Cr3InorpHtg_BmTF6B7C9pyzr9ycPmuO50UZ7TBLDE",
# }{
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1NjUwNTI4LCJpYXQiOjE3NDUyMTg0ODIsImp0aSI6IjVlOTk3NGFiMmI1NjQ4NWJhOTczZjRlYjdkMjllODkwIiwidXNlcl9pZCI6NX0.doQE4UZrIm25CAhDnqXSjvlxFAAAqrX2Io0txpKG86M"
# }