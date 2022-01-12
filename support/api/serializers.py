from django.contrib.auth import get_user_model
from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer, SerializerMethodField
from tickets.models import Tickets


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        queryset = model.objects.all()
        fields = ('id', 'email', 'password', 'name', 'support')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', '')
        user = self.Meta.model(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.set_password(validated_data.pop('password', ''))
        return super().update(instance, validated_data)


# class CommentSerializer(ModelSerializer):
#     replys = SerializerMethodField()
#
#     def get_replys(self, obj):
#         queryset = Comment.objects.filter(parent_id=obj.id)
#         serializer = CommentSerializer(queryset, many=True)
#         return serializer.data
#
#     class Meta:
#         model = Comment
#         fields = ('content', 'user', 'parent', 'replys')


class TicketListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='tickets-detail')
    client = SerializerMethodField(read_only=True)
    support_ticket = SerializerMethodField(read_only=True)
    comments = SerializerMethodField()

    def get_client(self, obj):
        # return str(obj.client.email)
        return str(obj.client)

    def get_support_ticket(self, obj):
        return str(obj.support_ticket)

    def get_comments(self, obj):
        pass

    #     queryset = Comment.objects.filter(ticket_id=obj.id, parent_id=None)
    #     serializer = CommentSerializer(queryset, many=True)
    #     return serializer.data

    class Meta:
        model = Tickets
        fields = ('id', 'title', 'url', 'client',
                  'support_ticket', 'comments', 'status')


class TicketDetailSerializer(ModelSerializer):
    client = SerializerMethodField(read_only=True)

    def get_client(self, obj):
        return str(obj.client.email)
        # return str(obj)

    class Meta:
        model = Tickets
        fields = ('title', 'text', 'client', 'status')
