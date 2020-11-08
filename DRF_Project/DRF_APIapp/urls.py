from django.urls import path
from .import views

urlpatterns = [
    path('student',views.studentView),
    path('student/<str:pk>',views.singleStudentView),
    path('studentPostView',views.studentPostView),
    path('studentupdate/<str:pk>',views.studentUpdateView),
    path('studentdelete/<str:pk>',views.studentDeleteView),
]