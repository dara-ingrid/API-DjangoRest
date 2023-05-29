from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewset, CursosViewset
from rest_framework import  routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewset, basename = 'Alunos')
router.register('cursos', CursosViewset, basename = 'Cursos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
