from django.urls import path ,include
from .views import CbvView , RedirectToGoogle , PostListView , PostDetailView , PostFormView 

app_name = 'blog'

urlpatterns = [
    path('cbv-templateview/',CbvView.as_view(),name='cbv-template'),
    path('cbv-redirectview/',RedirectToGoogle.as_view(),name='cbv-redirect'),
    path('cbv-listview/',PostListView.as_view(),name='cbv-list'),
    path('cbv-detailview/<int:test>/',PostDetailView.as_view(),name='cbv-detail'),
    path('cbv-formview/',PostFormView.as_view(),name='cbv-form'),
    path('api/v1/',include('blog.api.v1.urls')),

]