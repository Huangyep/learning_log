"""定义learning_logs的URL模式"""

from django.urls import path,re_path
from . import views

urlpatterns = [
    # 主页
    path('', views.index , name='index'),

    # 显示所有的主题
    path('topics/' , views.topics , name='topics'),

    # 显示主题的详细内容
    re_path('topics/(?P<topic_id>\d+)/' , views.topic , name='topic'),

]
app_name = 'learning_logs'