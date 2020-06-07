from rest_framework import serializers
from . models import Tree
from userprofile.serializers import UserProfileSerializer


class AllTreeSerializer(serializers.ModelSerializer):
	owner = UserProfileSerializer()

	class Meta:
		model = Tree
		fields = ["id",
			"name",
			"nickname",
			"details",
			"image",
			"family",
			"lat",
			"lng",
			"owner",
			"created_at",
			"broken",
			"approved",]