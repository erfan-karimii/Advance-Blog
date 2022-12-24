from django.urls import path 
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api_v1'

router = DefaultRouter()
router.register('post', views.PostModelViewSet,basename='post')
router.register('category', views.CategoryModelViewSet,basename='category')

urlpatterns = router.urls


# urlpatterns = [
#     # path('listview/',listView,name='listView'),
#     # path('detailview/<int:id>/',views.detailView,name='detailView')
#     path('listview/',views.PostList.as_view(),name='listView'),
#     path('detailview/<int:id>/',views.PostDetail.as_view(),name='listDetail'),
# ]