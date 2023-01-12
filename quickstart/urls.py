from django.urls import include, path
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'employees', views.EmployeeListViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('employee',views.Employeelist.as_view()),
    path('employee/<int:pk>', views.EmployeeDetails.as_view()),
    path('Amployee',views.Employee1list.as_view()),
    path('Amployee/<int:pk>', views.Employee1Details.as_view()),
]