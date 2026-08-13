from django.contrib import admin
from .models import Curso, Disciplina, DisciplinaTecnico, Atividade

admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(DisciplinaTecnico)
admin.site.register(Atividade)