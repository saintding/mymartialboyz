from martialboyzclub import models as mm

from rest_framework import serializers

class  collectionclass(serializers.ModelSerializer):

    class Meta:

        model = mm.collectionclass

        fields = "__all__"

class coachinfo(serializers.ModelSerializer):

    class Meta:

        model = mm.coachinfo

        fields = "__all__"

class pricecondition(serializers.ModelSerializer):

    class Meta:

        model = mm.pricecondition

        fields = "__all__"
        

