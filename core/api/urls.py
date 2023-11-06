from rest_framework import routers
from .viewsets import *

router = routers.SimpleRouter()
router.register(r"students", StudentViewSet, basename="students")
urlpatterns = [
    *router.urls,
]
