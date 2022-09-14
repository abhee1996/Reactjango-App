from django.urls  import path
from articles.api.views import *


# urlpatterns = [
#        path('articles', ArticleListView.as_view() name=""),
#        path('xyz', ArticleCreateView.as_view()),
#        #path('create', ArticleCreateView),
#        path('<pk>', ArticleDetailView.as_view()),
#        path('<pk>/update/', ArticleUpdateView),
#        path('<pk>/delete/', ArticleDeleteView)
#     ]

from articles.api import  views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.ArticleViewSet, basename='articles')
urlpatterns = router.urls

