from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Serie(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    serie = models.IntegerField()

    def __str__(self):
        return f"{self.serie}º ano"

class Disciplina(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    BIMESTRES = [
        ('1', 'Primeiro'),
        ('2', 'Segundo'),
        ('3', 'Terceiro'),
        ('4', 'Quarto'),
    ]

    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    valor = models.FloatField()
    bimestre = models.CharField(max_length=1, choices=BIMESTRES)

    def __str__(self):
        return self.nome

class Nota(models.Model):
    aluno = models.ForeignKey('usuario.Aluno',on_delete=models.CASCADE)
    atividade = models.ForeignKey(Atividade,on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=4,decimal_places=2)
