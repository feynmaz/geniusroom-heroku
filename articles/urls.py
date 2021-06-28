from django.urls import path, include

from .views import *


app_name = 'main'

urlpatterns = [
    path('', index, name='index'),

    path('<int:rubric_pk>/<int:pk>/', detail, name='detail'),
    path('<int:pk>/', by_rubric, name='by_rubric'),


    path('accounts/', include([

        path('login/', GRLoginView.as_view(), name='login'),
        path('logout/', GRLogoutView.as_view(), name='logout'),

        path('profile/<int:pk>/', profile_article_detail, name='profile_article_detail'),
        path('profile/', profile, name='profile'),
        path('profile/change/<int:pk>/', profile_article_change, name='profile_article_change'),
        path('profile/delete/<int:pk>/', profile_article_delete, name='profile_article_delete'),
        path('profile/change', ChangeUserInfoView.as_view(), name='profile_change'),
        path('profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
        path('profile/add', profile_article_add, name='profile_article_add'),

        path('password/change', GRPasswordChangeView.as_view(), name='password_change'),
        path('register/done', RegisterDoneView.as_view(), name='register_done'),
        path('register/activate/<str:sign>/', user_activate, name='register_activate'),
        path('register/', RegisterUserView.as_view(), name='register'),

    ])),

    path('<str:page>/', other_page, name='other'),
]