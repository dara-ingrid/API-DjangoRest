from rest_framework import viewsets
from escola.models import  Curso, Aluno
from serializer import AlunoSerializer, CursoSerializer

class AlunosViewset(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewset(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
