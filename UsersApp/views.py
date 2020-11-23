from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from UsersApp.usermodels import RetrieveAllUsers, CreateUser, UpdateUser, DeleteUserById
from UsersApp.companymodels import RetrieveAllCompanies, CreateCompany, UpdateCompany, DeleteCompanyById
from UsersApp.rolemodels import RetrieveAllRoles, CreateRole, UpdateRole, DeleteRoleById
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
@csrf_exempt
def UserApi(request,id=0):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        if CreateUser(user_data):
            return  JsonResponse("User Created", safe=False)
        return JsonResponse("Failed to Create User", safe=False)

    elif request.method == 'GET':
        return JsonResponse(RetrieveAllUsers(), safe=False)

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        if UpdateUser(user_data):
            return  JsonResponse("User Updated", safe=False)
        return JsonResponse("Failed to Update User", safe=False)

    elif request.method == 'DELETE':
        if DeleteUserById(id):
            return  JsonResponse("User Deleted", safe=False)
        return JsonResponse("User to Delete not Found", safe=False)

@csrf_exempt
def CompanyApi(request,id=0):
    if request.method == 'POST':
        company_data = JSONParser().parse(request)
        if CreateCompany(company_data):
            return  JsonResponse("Company Created", safe=False)
        return JsonResponse("Failed to Create Company", safe=False)

    elif request.method == 'GET':
        return JsonResponse(RetrieveAllCompanies(), safe=False)

    elif request.method == 'PUT':
        company_data = JSONParser().parse(request)
        if UpdateCompany(company_data):
            return  JsonResponse("Company Updated", safe=False)
        return JsonResponse("Failed to Update Company", safe=False)

    elif request.method == 'DELETE':
        if DeleteCompanyById(id):
            return  JsonResponse("Company Deleted", safe=False)
        return JsonResponse("Company to Delete not Found", safe=False)

@csrf_exempt
def RoleApi(request,id=0):
    if request.method == 'POST':
        role_data = JSONParser().parse(request)
        if CreateRole(role_data):
            return  JsonResponse("Role Created", safe=False)
        return JsonResponse("Failed to Create Role", safe=False)

    elif request.method == 'GET':
        return JsonResponse(RetrieveAllRoles(), safe=False)

    elif request.method == 'PUT':
        role_data = JSONParser().parse(request)
        if UpdateRole(role_data):
            return  JsonResponse("Role Updated", safe=False)
        return JsonResponse("Failed to Update Role", safe=False)

    elif request.method == 'DELETE':
        if DeleteRoleById(id):
            return  JsonResponse("Role Deleted", safe=False)
        return JsonResponse("Role to Delete not Found", safe=False)

@csrf_exempt
def UserRoleApi(request,id=0):
    if request.method == 'POST':
        userrole_data = JSONParser().parse(request)
        if CreateUserRole(userrole_data):
            return  JsonResponse("UserRole Created", safe=False)
        return JsonResponse("Failed to Create UserRole", safe=False)

    elif request.method == 'GET':
        return JsonResponse(RetrieveAllUserRoles(), safe=False)

    elif request.method == 'PUT':
        userrole_data = JSONParser().parse(request)
        if UpdateUserRole(userrole_data):
            return  JsonResponse("UserRole Updated", safe=False)
        return JsonResponse("Failed to Update UserRole", safe=False)

    elif request.method == 'DELETE':
        if DeleteUserRoleById(id):
            return  JsonResponse("UserRole Deleted", safe=False)
        return JsonResponse("UserRole to Delete not Found", safe=False)