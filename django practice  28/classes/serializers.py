from rest_framework import serializers
from .models import Classroom

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['name', 'capacity', 'department', 'area']

    def validate_capacity(self, value):
        if value < 5:
            raise serializers.ValidationError("ظرفیت کلاس باید حداقل ۵ باشد")
        return value

    def validate_area(self, value):
        if value < 0:
            raise serializers.ValidationError("مساحت نمی‌تواند منفی باشد")
        return value
