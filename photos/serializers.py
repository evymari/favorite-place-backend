"""from rest_framework import serializers
from .models import Event, EventRegistration


class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = ['id', 'event', 'child', 'user', 'registered_at']

    def validate(self, data):
        if 'event' not in data or 'child' not in data:
            raise serializers.ValidationError("Both 'event' and 'child' are required fields.")
        return data


class EventSerializer(serializers.ModelSerializer):
    registrations = EventRegistrationSerializer(many=True, read_only=True)
    remaining_spots = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'spots', 'remaining_spots', 'registrations']

    def get_remaining_spots(self, obj):
        return obj.spots - obj.registrations.count()"""