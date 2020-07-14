from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from api.models import Assessment, Question, Answer


class AssessmentNode(DjangoObjectType):
    class Meta:
        model = Assessment
        filter_fields = [
            'name',
        ]
        interfaces = (relay.Node, )


class QuestionNode(DjangoObjectType):
    class Meta:
        model = Question
        filter_fields = ['text', 'assessment','time']
        interfaces = (relay.Node, )


class AnswerNode(DjangoObjectType):
    class Meta:
        model = Answer
        filter_fields = ['text', 'question']
        interfaces = (relay.Node, )


class AssessmentQuery(ObjectType):
    assessment = relay.Node.Field(AssessmentNode)
    all_assessments = DjangoFilterConnectionField(AssessmentNode)
