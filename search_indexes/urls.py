from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from search_indexes.viewsets.exercise import ExerciseDocumentView

router = DefaultRouter()
exercises = router.register(r'exercises',
                            ExerciseDocumentView,
                            basename='exercisedocument')
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(router.urls))
]
