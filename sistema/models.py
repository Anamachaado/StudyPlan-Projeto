from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    disciplinas = models.ManyToManyField(
        'Disciplina',
        related_name='cursos'
    )

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class DisciplinaTecnico(Disciplina):
    cursos = models.ManyToManyField(
        Curso,
        related_name='disciplinas_tecnicas'
    )

    def __str__(self):
        return self.nome


class Atividade(models.Model):
    BIMESTRES = [
        ('1', 'Primeiro'),
        ('2', 'Segundo'),
        ('3', 'Terceiro'),
        ('4', 'Quarto'),
    ]

    disciplina = models.ForeignKey(
        'sistema.Disciplina',
        on_delete=models.CASCADE,
        related_name='atividades'
    )

    nome = models.CharField(max_length=100)
    valor = models.FloatField()
    bimestre = models.CharField(
        max_length=1,
        choices=BIMESTRES
    )

    def __str__(self):
        return self.nome