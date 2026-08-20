from django.contrib.auth.models import AbstractUser
from django.db import models

class Aluno(AbstractUser):
    curso = models.ForeignKey('sistema.Curso', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username