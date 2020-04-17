from django.urls import path

from members.apis import UserCreateView, UserRetrieveView, UserAuthTestAPIView

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('<int:pk>/', UserRetrieveView.as_view()),
    path('test/', UserAuthTestAPIView.as_view())

]
