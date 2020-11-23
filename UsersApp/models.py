from django.db import models

# Create your models here.
class Companies(models.Model):
    CompanyId = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=100)
    CompanyType = models.CharField(max_length=50)

class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=100)
    UserEmail = models.CharField(max_length=100)
    CompanyId = models.IntegerField(null=True)

class Roles(models.Model):
    RoleId = models.AutoField(primary_key=True)
    RoleName = models.CharField(max_length=100)
    Salary = models.FloatField()

class UserRoles(models.Model):
    UserRoleId = models.AutoField(primary_key=True)
    RoleId = models.IntegerField(null=True)
    UserId = models.IntegerField(null=True)