from asyncore import read
from rest_framework import serializers
from .models import CommentedItem, Question, Answer, Tag




class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='answer'
    )

    comments = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='comment'
    )

    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    content_object = serializers.StringRelatedField()

    class Meta:
        model = CommentedItem
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    comments = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='comment'
    )

    class Meta:
        model = Answer
        fields = '__all__'

