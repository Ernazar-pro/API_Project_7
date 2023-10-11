from app.models import User, Category, Create
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Create
        fields = (
            'id',
            'username',
            'password',
        )

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image = obj.image.url
            return request.build_absolute_uri(image)
        return None