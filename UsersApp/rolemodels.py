from UsersApp.serializers import RoleSeriallizer
from UsersApp.models import Roles

def RetrieveAllRoles():
    roles = Roles.objects.all()
    roles_seriallizer = RoleSeriallizer(roles, many = True)
    return roles_seriallizer.data

def CreateRole(role_data):
    roles_seriallizer = RoleSeriallizer(data=role_data)

    if roles_seriallizer.is_valid():
        roles_seriallizer.save()
        return True

    return False

def UpdateRole(role_data):
    role = Roles.objects.get(RoleId=role_data['RoleId'])
    roles_seriallizer = RoleSeriallizer(role, data=role_data)
    
    if roles_seriallizer.is_valid():
        roles_seriallizer.save()
        return True

    return False

def DeleteRoleById(id):
    role = Roles.objects.get(RoleId=id)
    role.delete()
    return True



