from django.test import TestCase
from rest_framework.test import APIClient
from stackoverflow.models import Answer, Question, Tag, CommentedItem


class TestStackoverflowQuestion(TestCase):
    '''
        Class under test : Question
        This is to demonstrate TDD so we can make CICD full automated and assue quality.
    '''

    def setUp(self) -> None:
        '''
            This method runs before every test case
        '''
        self.client = APIClient()

    # questions basic tests
    # Index

    def test_questions_can_be_retreived(self):
        res = self.client.get('/questions/')
        assert res.status_code == 200

    # Show
    def test_a_quesion_can_be_retreived(self):
        question = Question.objects.create(question="what is your fav color?")
        res = self.client.get(f'/questions/{question.id}/')
        assert res.status_code == 200

    # Create
    def test_a_quesion_can_be_created(self):
        res = self.client.post(
            f'/questions/', {'question': 'What is you fav language'},  format='json')
        assert res.status_code == 201

    # Update
    def test_a_quesion_can_be_updated(self):
        question = Question.objects.create(question="what is your fav color?")
        res = self.client.put(
            f'/questions/{question.id}/', {'question': 'What is you fav language'},  format='json')
        assert res.status_code == 200

    def test_a_quesion_can_be_updated_content(self):
        question = Question.objects.create(question="what is your fav color?")
        res = self.client.put(
            f'/questions/{question.id}/', {'question': 'What is you fav language'},  format='json')
        self.assertContains(response=res, text='What is you fav language') 

    # Delete
    def test_a_quesion_can_be_deleted(self):
        question = Question.objects.create(question="what is your fav color?")
        res = self.client.delete(f'/questions/{question.id}/')
        assert res.status_code == 204

    # Relationship -> Answer
    def test_question_have_answers(self):
        question = Question.objects.create(question="what is your fav color?")
        res = self.client.get(f'/questions/{question.id}/answers/')
        assert res.status_code == 200

    def test_answer_can_be_created_for_a_question(self):
        question = Question.objects.create(question="what is your fav color?")
        res = self.client.post(
            f'/questions/{question.id}/answers/', {'answer': 'my answer'},  format='json')
        assert res.status_code == 201

    # Relationship -> Comment
    def test_question_have_comments(self):
        question = Question.objects.create(question="what is your fav color?")
        res = self.client.get(f'/questions/{question.id}/comments/')
        assert res.status_code == 200

    def test_comment_can_be_created_for_a_question(self):
        question = Question.objects.create(question="what is your fav color?")
        res = self.client.post(
            f'/questions/{question.id}/comments/', {'comment': 'nice question'},  format='json')
        assert res.status_code == 201

    # Relationship -> Tags
    def test_question_have_tags(self):
        question = Question.objects.create(question="what is your fav color?")
        res = self.client.get(f'/questions/{question.id}/tags/')
        assert res.status_code == 200


class TestStackoverflowAnswer(TestCase):
    '''
        Class under test : Answer
        This is to demonstrate TDD so we can make CICD full automated and assue quality.
    '''

    def setUp(self) -> None:
        '''
            This method runs before every test case
        '''
        self.client = APIClient()

    # answers basic test
    # Index
    def test_answers_can_be_retreived(self):
        res = self.client.get(f'/answers/')
        assert res.status_code == 200

    # Show
    def test_an_answer_can_be_retreived(self):
        question = Question.objects.create(question="what is your fav color?")
        answer = Answer.objects.create(
            answer="my answer", question_id=question.id)
        res = self.client.get(f'/answers/{answer.id}/')
        assert res.status_code == 200

    # Create
    def test_an_answer_can_be_created(self):
        question = Question.objects.create(question="what is your fav color?")
        res = self.client.post(
            f'/answers/', {'answer': 'What is you fav language', 'question': question.id},  format='json')
        assert res.status_code == 201

    # update
    def test_an_answer_can_be_update(self):
        question = Question.objects.create(question="what is your fav color?")
        answer = Answer.objects.create(
            answer="my answer", question_id=question.id)
        res = self.client.patch(
            f'/answers/{answer.id}/', {'answer': 'my answer is no'},  format='json')
        assert res.status_code == 200

    def test_an_answer_can_be_update_content(self):
        question = Question.objects.create(question="what is your fav color?")
        answer = Answer.objects.create(
            answer="my answer", question_id=question.id)
        res = self.client.patch(
            f'/answers/{answer.id}/', {'answer': 'my answer is no'},  format='json')
        self.assertContains(response=res, text='my answer is no') 

    # Delete
    def test_an_answer_can_be_deleted(self):
        question = Question.objects.create(question="what is your fav color?")
        answer = Answer.objects.create(
            answer="my answer", question_id=question.id)
        res = self.client.delete(f'/answers/{answer.id}/')
        assert res.status_code == 204


    # Relationship -> Question
    def test_answer_belong_to_question(self):
        question = Question.objects.create(question="what is your fav color?")
        answer = Answer.objects.create(
            answer="my answer", question_id=question.id)
        res = self.client.get(f'/answers/{answer.id}/question/')
        self.assertContains(response=res, text=question.id)


    # Relationship -> Comment
    def test_answer_have_comments(self):
        question = Question.objects.create(question="what is your fav color?")
        answer = Answer.objects.create(
            answer="my answer", question_id=question.id)
        comment = answer.comments.create(comment='nice answer')
        res = self.client.get(f'/answers/{answer.id}/comments/')
        self.assertContains(response=res, text=comment.comment)

    def test_comment_can_be_created_for_a_answer(self):
        question = Question.objects.create(question="what is your fav color?")
        answer = Answer.objects.create(
            answer="my answer", question_id=question.id)
        res = self.client.post(
            f'/answers/{answer.id}/comments/', {'comment': 'nice answer'},  format='json')
        assert res.status_code == 201


class TestStackoverflowComment(TestCase):
    '''
        Class under test : Comment
        This is to demonstrate TDD so we can make CICD full automated and assue quality.
    '''

    def setUp(self) -> None:
        '''
            This method runs before every test case
        '''
        self.client = APIClient()

    # comment basic test
    # Index
    def test_comment_can_be_retreived(self):
        res = self.client.get(f'/comments/')
        assert res.status_code == 200

    # Show
    def test_a_comment_can_be_retreived(self):
        question = Question.objects.create(question="what is your fav color?")
        comment = CommentedItem.objects.create(
            comment="I'm comment", content_object=question)
        res = self.client.get(f'/comments/{comment.id}/')
        assert res.status_code == 200

    # Create
    def test_a_comment_can_be_created_for_question(self):
        question = Question.objects.create(question="what is your fav color?")
        res = self.client.post(
            f'/questions/{question.id}/comments/', {'comment': 'nice question'},  format='json')
        self.assertContains(response=res, text='nice question',status_code=201)

    # update
    def test_an_answer_can_be_update(self):
        question = Question.objects.create(question="what is your fav color?")
        comment = CommentedItem.objects.create(
            comment="I'm comment", content_object=question)
        res = self.client.patch(f'/comments/{comment.id}/', {'comment': 'nice question'},  format='json')
        assert res.status_code == 200

    def test_an_answer_can_be_update_content(self):
        question = Question.objects.create(question="what is your fav color?")
        comment = CommentedItem.objects.create(
            comment="I'm comment", content_object=question)
        res = self.client.patch(f'/comments/{comment.id}/', {'comment': 'nice question'},  format='json')
        self.assertContains(response=res, text='nice question')

    # Delete
    def test_an_answer_can_be_deleted(self):
        question = Question.objects.create(question="what is your fav color?")
        comment = CommentedItem.objects.create(
            comment="I'm comment", content_object=question)
        res = self.client.delete(f'/comments/{comment.id}/')
        assert res.status_code == 204
