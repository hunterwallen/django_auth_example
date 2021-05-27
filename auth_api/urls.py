from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/useraccount', views.UserAccountList.as_view(), name='useraccount_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/useraccount/<int:pk>', views.UserAccountDetail.as_view(), name='useraccount_detail'), # api/contacts will be routed to the ContactDetail view for handling
    path('api/useraccount/login', csrf_exempt(views.check_login), name="check_login")
]
