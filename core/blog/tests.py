# from django.test import TestCase , SimpleTestCase 
import pytest
from django.urls import reverse , resolve
from .views import PostListView
# Create your tests here.

class TestUrl:
    def test_cbv_list_blog_url(self):
        url = reverse('blog:cbv-list')
        assert resolve(url).func.view_class == PostListView , 'error'
