from rest_framework.generics import ListAPIView
from . models import Tree
from . serializers import AllTreeSerializer
# Create your views here.


class TreeList(ListAPIView):
	serializer_class = AllTreeSerializer
	queryset  = Tree.objects.filter(approved=True)

