from django.contrib.auth.models import AbstractUser
from django.db import models

class Aluno(AbstractUser):

    curso = models.ForeignKey(
        'sistema.Curso',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username