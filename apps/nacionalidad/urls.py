from django.conf.urls import url
from apps.nacionalidad.views import index, nacionalidad_view

urlpatterns = [
    url(r'^index$', index, name='index'),
    url(r'^nuevo$',nacionalidad_view, name='nueva_nacionalidad'),
    url(r'^nacionalidad/nuevo$',nacionalidad_view, name='nueva_nacionalidad'),

]