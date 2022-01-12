from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from api.serializers import TicketDetailSerializer, TicketListSerializer, UserSerializer
from api.permissions import IsAuthorOrReadOnly
from tickets.models import Tickets


class UserViewSet(ModelViewSet):
    model = get_user_model()
    queryset = model.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class TicketViewSet(ModelViewSet):
    model = Tickets
    queryset = model.objects.none()
    serializer_class = TicketDetailSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_serializer_class(self):
        if self.action == 'list':
            return TicketListSerializer
        return TicketDetailSerializer

    def get_queryset(self):
        if self.request.user.admin:
            return self.model.objects.all()
        return self.model.objects.filter(client=self.request.user)

    def perform_create(self, serializer):
        # serializer.save(client=self.request.user) # Вернуть, это если не сработает нижний
        serializer.validated_data['client'] = self.request.user
        serializer.save()

# class CommentViewSet(ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#
#     def get_queryset(self):
#         ticket_id = self.kwargs["id"]
#         queryset = Comment.objects.filter(ticket__id=ticket_id)
#         return queryset
