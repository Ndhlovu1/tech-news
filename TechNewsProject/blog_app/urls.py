from django.urls import path
from . import views

#TODO
app_name = 'blog_app'

urlpatterns = [
    #post views
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]

# year  : Needs an int
# month : Needs an int 
# day   : Needs an int
# post  : Can be composed of words and hyphens
