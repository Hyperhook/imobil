from django.conf.urls import url
from .views import ProprietarioCreate, ProprietarioList

urlpatterns = [
    url(r'^proprietarios/add/', ProprietarioCreate.as_view(), name='proprietario-add'),
    url(r'^', ProprietarioList.as_view(), name='proprietario-view')
]