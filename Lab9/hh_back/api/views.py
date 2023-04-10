from django.http import JsonResponse

from .models import Company, Vacancy


def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all().values()
        return JsonResponse({'companies': list(companies)})


def company_detail(request, id):
    if request.method == 'GET':
        company = Company.objects.filter(id=id).values()
        return JsonResponse({'company': list(company)})



def company_vacancies(request, id):
    if request.method == 'GET':
        company = Company.objects.get(id=id)
        vacancies = Vacancy.objects.filter(company=company).values()
        return JsonResponse({'vacancies': list(vacancies)})


def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all().values()
        return JsonResponse({'vacancies': list(vacancies)})


def vacancy_detail(request, id):
    if request.method == 'GET':
        vacancy = Vacancy.objects.filter(id=id).values()
        return JsonResponse({'vacancy': list(vacancy)})


def top_ten_vacancies(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.order_by('-salary')[:10].values()
        return JsonResponse({'top_ten_vacancies': list(vacancies)})
