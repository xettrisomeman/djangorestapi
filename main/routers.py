from rest_framework import routers

from newapp.apiviews import (
    TheoryViewSet,
    ScientistViewSet
)

router = routers.DefaultRouter()


router.register('theory' , TheoryViewSet,basename='theory')
router.register('scientist' , ScientistViewSet , basename='scientist')


urlpatterns = router.urls

