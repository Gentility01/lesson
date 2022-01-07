from django.urls import path
from .views import(
    # my_fbv,
    CourseView,
    CourseListView,
    # CourseFilterView
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView
    )

urlpatterns = [
    # path('', my_fbv, name='my_fbv')
    path('', CourseView.as_view(), name='my_fbv'),
    path('create/', CourseCreateView.as_view(), name='coursecreate'),
    # path('filter', CourseFilterView.as_view(), name='coursefiler'),
    path('list/', CourseListView.as_view(), name='courselist'),
    path('<int:id>/', CourseView.as_view(), name='coursedetail'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='courseupdate'),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name='coursedelete'),
]

