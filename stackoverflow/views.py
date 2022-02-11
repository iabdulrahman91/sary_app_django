from .serializers import AnswerSerializer, CommentSerializer, QuestionSerializer, TagSerializer
from .models import Answer, CommentedItem, Question, Tag
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(detail=True, methods=['GET', 'POST'])
    def answers(self, request, *args, **kwargs):
        if request.method == 'GET':
            queryset = self.get_object().answers.all()
            serializer = AnswerSerializer(queryset, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = AnswerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(question=self.get_object())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['GET', 'POST'])
    def comments(self, request, *args, **kwargs):
        if request.method == 'GET':
            queryset = self.get_object().comments.all()
            serializer = CommentSerializer(queryset, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(question=self.get_object())
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['GET'])
    def tags(self, request, *args, **kwargs):
        if request.method == 'GET':
            queryset = self.get_object().tags.all()
            serializer = TagSerializer(queryset, many=True)
            return Response(serializer.data)
        elif request.method == 'POST': # might be use later
            serializer = TagSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                self.get_object().tags.add(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class AnswerView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    @action(detail=True, methods=['GET'])
    def question(self, request, *args, **kwargs):
        query = self.get_object().question
        serializer = QuestionSerializer(query, many=False)
        return Response(serializer.data)

    @action(detail=True, methods=['GET', 'POST'])
    def comments(self, request, *args, **kwargs):
        if request.method == 'GET':
            queryset = self.get_object().comments.all()
            serializer = CommentSerializer(queryset, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(answer=self.get_object())
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentView(viewsets.ModelViewSet):
    queryset = CommentedItem.objects.all()
    serializer_class = CommentSerializer


class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
    @action(detail=True, methods=['GET'])
    def questions(self, request, *args, **kwargs):
        if request.method == 'GET':
            queryset = self.get_object().questions.all()
            serializer = QuestionSerializer(queryset, many=True)
            return Response(serializer.data)
