from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404
from .models import Organization


def index(request):
    org_list = Organization.objects.order_by('created_at')
    context = {
        'org_list': org_list,
    }
    return render(request, 'crm/index.html', context)


def organization(request, organization_id):
    name = get_object_or_404(Organization, pk=organization_id)
    # created_at = Organization.objects.get('scheduled_at')
    context = {
            'name': name,
            # 'created_at': created_at,
        }
    return render(request,'crm/detail.html', context)


def customer(request, customer_id):
    response = "You're looking at customer ID:  %s"
    return HttpResponse(response % customer_id)
#
# def job(request):
#     return HttpResponse("You're voting on question %s." % job_id)

