#added by me
from rest_framework import serializers
from .models import Link

#created by
class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"

