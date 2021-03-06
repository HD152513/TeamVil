from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('member_detail/<int:profile_id>', views.member_detail, name = "member_detail"),
    path('member_search/', views.member_search, name = "member_search"),
    path('member_search_back/', views.member_search_back, name = "member_search_back"),
    path('member_search_back_cloud/', views.member_search_back_cloud, name = "member_search_back_cloud"),
    path('member_detail_back/<int:profile_id>', views.member_detail_back, name = "member_detail_back"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    # path('signup_back/', views.signup, name="signup"),
    # path('login_back/', views.login, name="login"),
    path('logout_back/',views.logout_back, name="logout"),
    path('mypage_profile_back', views.mypage_profile, name="mypage_profile"),
    path('mypage_project_back', views.mypage_project, name="mypage_project"),
    path('searchMember/', views.searchMember, name="searchMember"),
    path('filterMember/', views.filterMember, name="filterMember"),
    path('latestMember/', views.latestMember, name="latestMember"),
    path('mypage_modify_profile_back_sunneng', views.mypage_modify_profile_edit, name="mypage_modify_profile_edit"),
    path('mypage_modify_profile_back_sunneng/update', views.mypage_modify_profile_update, name="mypage_modify_profile_update"),
    path('mypage', views.mypage, name = 'mypage'),
    path('mypage_profile', views.mypage_profile, name = 'mypage_profile'),
    path('mypage_project', views.mypage_project, name = 'mypage_project'),
    path('mypage_modify_profile', views.mypage_modify_profile, name = 'mypage_modify_profile'),
    path('mypage_like', views.mypage_like, name = 'mypage_like'),
    path('mypage_scrap', views.mypage_scrap, name = 'mypage_scrap'),
    path('like/', views.likes, name="likes"),
    path('likecancel/',views.likecancels, name="likecancels"),
    path('alarm_detail/', views.alarm_detail, name = "alarm_detail"),
    path('message/', views.message, name="message"),
    #path('member_state/<int:state_id>', views.member_state, name ="member_state")
]