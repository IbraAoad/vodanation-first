from django.shortcuts import render , get_object_or_404, redirect
from ro_app.forms import SiteForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

from ro_app.models import SiteData, SiteInfo

from django.http import JsonResponse
import json




@login_required
def add_view(request): 
    site_form = SiteForm()
    if request.method == 'POST':
        site_form = SiteForm(request.POST)

        if site_form.is_valid():
            site_form.save(commit=False)
            email_submitted = request.POST.get('product')
            siteid_submitted = site_form.cleaned_data['site_id']
            site_form.instance.email_address = email_submitted

            try:
                obj_filtered = SiteInfo.objects.get(email_address=email_submitted)
                staff_id_value = getattr(obj_filtered, 'staff_id')
            except ObjectDoesNotExist:
                staff_id_value = "NANA"
            site_form.instance.staff_id = staff_id_value

            try:
                obj_filtered = SiteInfo.objects.get(site_id=siteid_submitted)
                area_value = getattr(obj_filtered, 'area')
                rt_gf_value = getattr(obj_filtered, 'rt_gf')
                str_type_value = getattr(obj_filtered, 'str_type')
                height_value = getattr(obj_filtered, 'height')
            except ObjectDoesNotExist:
                area_value = "NANA"
                rt_gf_value = "NANA"
                str_type_value = "NANA"
                height_value = "NANA"

            site_form.instance.area = area_value
            site_form.instance.rt_gf = rt_gf_value
            site_form.instance.str_type = str_type_value
            site_form.instance.height = height_value

            if str(site_form.cleaned_data['status']) == "Pending":
                site_form.instance.in_progress_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            elif str(site_form.cleaned_data['status']) == "Done":
                site_form.instance.done_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            site_form.save(commit=True)
            return redirect('search')

    return render( request, "ro_app/ro_main.html", {'form': site_form})

@login_required
def update_view(request, pk):
    context = {}
    obj = get_object_or_404(SiteData, id = pk)
    site_form = SiteForm(request.POST or None, instance = obj) 
    if site_form.is_valid():
        site_form.save(commit=False)
        if site_form.cleaned_data['status'] == "Pending":
            site_form.instance.in_progress_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        elif site_form.cleaned_data['status'] == "Done":
            site_form.instance.done_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        site_form.save(commit=True)
        return redirect('search')
    context["form"] = site_form 
    return render(request, "ro_app/ro_main.html", context) 

@login_required
def site_remove(request, pk):
    site = get_object_or_404(SiteData, pk=pk)
    site.delete()
    return redirect('search')


class SearchView(ListView):
    model = SiteData
    template_name = 'ro_app/ro_main.html'
    context_object_name = 'all_search_results'


class SiteDetailView(DetailView):
    model = SiteData
    template_name = 'ro_app/ro_main.html'
    context_object_name = 'site_details'

def autocomplete(request):
    if 'term' in request.GET:
        qs = SiteInfo.objects.filter(email_address__icontains=request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.append(product.email_address)
        return JsonResponse(titles, safe=False)
    return render(request, 'ro_app/ro_main.html')