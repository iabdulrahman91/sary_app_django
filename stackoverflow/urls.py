from rest_framework import routers
from . import views

app_name = 'stackoverflow'
router = routers.DefaultRouter()
router.register(r'questions', views.QuestionView, basename='question')
router.register(r'answers', views.AnswerView, basename='answer')
router.register(r'comments', views.CommentView, basename='comment')
router.register(r'tags', views.TagView, basename='tag')

urlpatterns = router.urls

