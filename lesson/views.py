from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Lesson
from .serializers import LessonSerializer


@api_view(['GET'])
def get_lessons(requset):
    """view to see all the lessons"""
    
    lessons = Lesson.objects.all()
    lessons_serializer = LessonSerializer(lessons, many=True)
    
    return Response(lessons_serializer.data)


@api_view(['GET'])
def get_lesson(requset, lesson_id):
    """view to see selected lesson"""
    
    lesson = Lesson.objects.get(pk=lesson_id)
    lessons_serializer = LessonSerializer(lesson)
    
    return Response(lessons_serializer.data)
    