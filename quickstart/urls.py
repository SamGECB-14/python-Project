from django.urls import include, path
from rest_framework import routers
from quickstart import views
# from .views import MyTokenObtainPairView
from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework_simplejwt.views import (
#     TokenRefreshView,
# )






router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'student', views.StudentViewset)
router.register(r'song', views.SongViewSet)
router.register(r'singer', views.SingerViewSet)

router.include_format_suffixes = False

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('v1', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('employee',views.Employeelist.as_view()),
    path('employee/<int:pk>', views.EmployeeDetails.as_view()),
    path('Amployee',views.Employee1list.as_view()),
    path('Amployee/<int:pk>', views.Employee1Details.as_view()),
    path('student', views.student_list),
    path('student/<int:pk>', views.student_detail),
    path('st', views.studentlist.as_view()),
    path('st/<int:pk>', views.studentdetails.as_view()),
    # path('api/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
urlpatterns = format_suffix_patterns(urlpatterns)
