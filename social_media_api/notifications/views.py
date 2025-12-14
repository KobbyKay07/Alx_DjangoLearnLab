from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import Notification
from .serializers import NotificationSerializer

# Create your views here.

class NotificationListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)
