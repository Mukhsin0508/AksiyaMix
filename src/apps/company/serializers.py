from rest_framework import serializers

from apps.general.locations import Location
from .models import *



class CompanyLocationSerializer(serializers.ModelSerializer):
    region = serializers.MultipleChoiceField(choices=[])
    district = serializers.MultipleChoiceField(choices=[])

    class Meta:
        model = CompanyLocation
        fields = "__all__"

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.fields['region'].choices = Location.get_region_choices()

        # if we are updating an instance, populate the district field with the districts of the region
        if self.instance:
            self.fields['district'].choices = Location.get_districts_by_regions(self.instance.region_id)

    def validate(self, data):
        region = data.get('region')
        if region:
            data['district'] = Location.get_districts_by_regions(region)
        return data

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['region'] = dict(Location.get_region_choices())[instance.region]
        rep['district'] = dict(Location.get_districts_by_regions(instance.region_id))[instance.district]
        return rep


class CompanySerializer(serializers.ModelSerializer):
    """ Company serializer """

    class Meta:
        model = Company
        fields = "__all__"


class CompanyTimeTableSerializer(serializers.ModelSerializer):
    """ Company timetable serializer """

    class Meta:
        model = CompanyTimeTable
        fields = "__all__"


