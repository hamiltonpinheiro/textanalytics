from rest_framework import routers

from . import views as sort_views

router = routers.DefaultRouter()

router.register(r'document', sort_views.DocumentViewset)


router.register(r'documentclassification', sort_views.DocumentClassificationViewset)

