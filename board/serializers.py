from board.models import *
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):

    class Meta:  
        model = Comment  
        fields = ['title', ]

class AdvertSerializer(serializers.ModelSerializer):

    # comments = CommentSerializer() 


    class Meta:  
        model = Advert  
        fields = ['id', 'title', 'body', 'date_adv', 'tags']

    # def create(self, validated_data):
    #     comment_data = validated_data.get('comments')
    #     comment = Comment.objects.create(**comment_data)
    #     validated_data['comments'] = comment
    #     advert = Advert.objects.create(**validated_data)
        
    #     return advert


class TagSerializer(serializers.ModelSerializer):

    class Meta:  
        model = Tag  
        fields = '__all__'