from django.urls import path 
from . import views
urlpatterns = [
    path('submission/',views.SubmitAssignment.as_view() ),
    path('enroleCourse/',views.EnroleToCourse.as_view() ),
    path('getLessons/<int:course_id>/',views.GetCourseVideos.as_view()),
]
