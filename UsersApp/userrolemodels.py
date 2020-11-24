from UsersApp.serializers import UserRoleSeriallizer
from UsersApp.models import UserRoles

def RetrieveAllUserRoles():
    userroles = UserRoles.objects.all()
    userroles_seriallizer = UserRoleSeriallizer(userroles, many = True)
    return userroles_seriallizer.data

def CreateUserRole(role_data):
    userroles_seriallizer = UserRoleSeriallizer(data=role_data)

    if userroles_seriallizer.is_valid():
        userroles_seriallizer.save()
        return True

    return False

def UpdateRole(role_data):
    userrole = UserRoles.objects.get(RoleId=role_data['userroleId'])
    userroles_seriallizer = UserRoleSeriallizer(userrole, data=role_data)
    
    if userroles_seriallizer.is_valid():
        userroles_seriallizer.save()
        return True

    return False

def DeleteUserRoleById(id):
    userrole = UserRoles.objects.get(RoleId=id)
    userrole.delete()
    return True



