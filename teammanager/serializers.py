from rest_framework import serializers
from teammanager.models import *
from collections import OrderedDict


class ChoicesField(serializers.Field):
    """Custom ChoiceField serializer field."""

    def __init__(self, choices, **kwargs):
        """init."""
        self._choices = OrderedDict(choices)
        super(ChoicesField, self).__init__(**kwargs)

    def to_representation(self, obj):
        """Used while retrieving value for the field."""
        return self._choices[obj]

    def to_internal_value(self, data):
        """Used while storing value for the field."""
        for i in self._choices:
            if self._choices[i] == data:
                return i
        raise serializers.ValidationError("Acceptable values are {0}.".format(list(self._choices.values())))

class MemberSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    role = ChoicesField(Member.ROLE_CHOICES)
    
    def get_role(self,obj):
        return obj.get_role_display()
    
    class Meta:
        model = Member
        fields = ('id','first_name','last_name','phoneno','email','role')