from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.ForeignKey("Role", on_delete=models.CASCADE)


class Role(models.Model):
    role_name = models.CharField(max_length=10)

    def __str__(self):
        return self.role_name