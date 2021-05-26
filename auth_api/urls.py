from django.urls import path
from . import views

urlpatterns = [
    path('api/useraccount', views.UserAccountList.as_view(), name='useraccount_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/useraccount/<int:pk>', views.UserAccountDetail.as_view(), name='useraccount_detail'), # api/contacts will be routed to the ContactDetail view for handling
    path('api/useraccount/login', views.UserAccountLogin.as_view(), name='useraccount_login'),
    path('api/useraccount/login/<int:pk>', views.UserAccountLoginDetail.as_view(), name='useraccountlogin_detail')
]
