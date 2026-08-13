from django.contrib import admin
from .models import Curso, Disciplina, DisciplinaTecnico, Atividade


class DisciplinaTecnicoInline(admin.TabularInline):
    model = DisciplinaTecnico.cursos.through
    extra = 0


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    filter_horizontal = ('disciplinas',)
    inlines = [DisciplinaTecnicoInline]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        form.base_fields['disciplinas'].queryset = Disciplina.objects.exclude(
            disciplinatecnico__isnull=False
        )

        return form

admin.site.register(Disciplina)
admin.site.register(DisciplinaTecnico)
admin.site.register(Atividade)