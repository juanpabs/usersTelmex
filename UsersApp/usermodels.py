from UsersApp.serializers import UserSeriallizer
from UsersApp.models import Users

def RetrieveAllUsers():
    users = Users.objects.all()
    users_seriallizer = UserSeriallizer(users, many = True)
    return users_seriallizer.data

def CreateUser(user_data):
    users_seriallizer = UserSeriallizer(data=user_data)

    if users_seriallizer.is_valid():
        users_seriallizer.save()
        return users_seriallizer.data

    return None

def UpdateUser(user_data):
    user = Users.objects.get(UserId=user_data['UserId'])
    users_seriallizer = UserSeriallizer(user, data=user_data)
    
    if users_seriallizer.is_valid():
        users_seriallizer.save()
        return True

    return False

def DeleteUserById(id):
    user = Users.objects.get(UserId=id)
    user.delete()
    return True



