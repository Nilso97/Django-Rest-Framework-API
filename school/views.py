from rest_framework import viewsets, generics
from school.models import Student, Course, Enrollment
from rest_framework.authentication import BasicAuthentication 
from rest_framework.permissions import IsAuthenticated
from school.serializer import StudentSerializer, CourseSerializer, EnrollmentSerializer, ListEnrolledStudentSerializer,ListStudentsEnrolledInCourseSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    """Exibir todos os alunos(as) cadastrados"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    permission_classes = [IsAuthenticated]
    authentication_class = [BasicAuthentication]

class CoursesViewSet(viewsets.ModelViewSet):
    """Exibir todos os cursos cadastrados"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    permission_classes = [IsAuthenticated]
    authentication_class = [BasicAuthentication]

class EnrollmentsViewSet(viewsets.ModelViewSet):
    """Listando todas as matrículas"""
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

    permission_classes = [IsAuthenticated]
    authentication_class = [BasicAuthentication]

class ListEnrolledStudentViewSet(generics.ListAPIView):
    """Listando as matrículas de um aluno(a)"""

    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListEnrolledStudentSerializer

    permission_classes = [IsAuthenticated]
    authentication_class = [BasicAuthentication]

class ListStudentsEnrolledInCourseViewSet(generics.ListAPIView):
    """Listando os alunos(as) matrículados em um curso"""

    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListStudentsEnrolledInCourseSerializer

    permission_classes = [IsAuthenticated]
    authentication_class = [BasicAuthentication]

