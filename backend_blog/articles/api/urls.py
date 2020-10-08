# from django.urls  import path
# from . import views

# urlpatterns = [
#      path('articles', views.ArticleView.as_view()),
#      path('create', views.ArticleView.as_view()),
#      path('<pk>', views.ArticleView.as_view()),
#      path('<pk>/update/', views.ArticleView.as_view()),
#      path('<pk>/delete/', views.ArticleView.as_view())
#   ]
from articles.api.views import ArticleViewSet
#from articles.api.views import ArticleView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ArticleViewSet, basename='articles')
urlpatterns = router.urls

