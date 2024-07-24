from django.urls import path
from .views import register, login_view,success_view
from .views import AdminOnlyView, ManagerOnlyView

urlpatterns = [
    path('signup/', register, name='signup'),
    path('login/', login_view, name='login'),
    path('success/', success_view, name='success'),
    path('admin-view/', AdminOnlyView.as_view(), name='admin-view'),
    path('manager-view/', ManagerOnlyView.as_view(), name='manager-view'),
]
