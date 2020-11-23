from UsersApp.serializers import CompanySeriallizer
from UsersApp.models import Companies

def RetrieveAllCompanies():
    companies = Companies.objects.all()
    companies_seriallizer = CompanySeriallizer(companies, many = True)
    return companies_seriallizer.data

def CreateCompany(company_data):
    companies_seriallizer = CompanySeriallizer(data=company_data)

    if companies_seriallizer.is_valid():
        companies_seriallizer.save()
        return True

    return False

def UpdateCompany(company_data):
    company = Companies.objects.get(CompanyId=company_data['CompanyId'])
    companies_seriallizer = CompanySeriallizer(company, data=company_data)
    
    if companies_seriallizer.is_valid():
        companies_seriallizer.save()
        return True

    return False

def DeleteCompanyById(id):
    company = Companies.objects.get(CompanyId=id)
    company.delete()
    return True



