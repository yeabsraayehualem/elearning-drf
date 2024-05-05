from django.urls import path
from . import views 
urlpatterns = [
    
    path('update_course_status/<int:id>/<str:status>',views.ApproveCourses().as_view()),
    path('update_user_status/<int:id>/<str:role>',views.UpdateUser().as_view())

]
