from rest_framework import routers
from .viewsets import *

router = routers.SimpleRouter()
router.register("students", StudentViewSet, basename="students")
urlpatterns = router.urls
