from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField()
    following_count = serializers.IntegerField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers_count', 'following_count']

    def followers_count(self, obj):
        return obj.followers.count()
    
    def following_count(self, obj):
        return obj.following.count()
    

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise AuthenticationFailed("Invalid email or password.")
        data['user'] = user
        return data