from rest_framework import serializers
from UsersApp.models import Users, Companies, Roles, UserRoles

class UserSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('UserId',
                    'UserName',
                    'UserEmail',
                    'CompanyId')

class CompanySeriallizer(serializers.ModelSerializer):
    class Meta:
        model  = Companies
        fields = ('CompanyId',
                    'CompanyName',
                    'CompanyType')

class RoleSeriallizer(serializers.ModelSerializer):
    class Meta:
        model  = Roles
        fields = ('RoleId',
                    'RoleName',
                    'Salary')

class UserRoleSeriallizer(serializers.ModelSerializer):
    class Meta:
        model  = UserRoles
        fields = ('UserRoleId',
                    'UserId',
                    'RoleId')