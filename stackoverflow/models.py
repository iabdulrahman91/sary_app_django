from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey


class CommentedItem(models.Model):
    """
    Comments arbitrary model instances using a generic relation.
    See: https://docs.djangoproject.com/en/stable/ref/contrib/contenttypes/
    """
    comment = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.comment


class Question(models.Model):
    question = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    comments = GenericRelation(CommentedItem)  # POLYMORPHIC

    def __str__(self):
        return self.question


class Answer(models.Model):
    answer = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    comments = GenericRelation(CommentedItem, related_query_name='comments')  # POLYMORPHIC
    # one-to-many relationship (Answer belong to one Question, and a Question can have many Answers)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    def __str__(self):
        return self.answer


class Tag(models.Model):
    tag =  models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    # many-to-many relationship (Tag can belong to one or many Questions, and a Question can have one or many Tags)
    questions = models.ManyToManyField(Question, related_name='tags', blank=True)

    def __str__(self):
        return self.tag
