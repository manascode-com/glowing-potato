from django.urls import path
from . views import TreeList


urlpatterns = [
	path('trees/', TreeList.as_view(), name='tree_list' )
]