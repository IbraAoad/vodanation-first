from django.shortcuts import render , get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from ro_app.models import ConsVals,ReqVals,StatVals,SiteVals,BuilVals,ActVals,StarVals,SiteData, SiteInfo
from django.http import JsonResponse
import json

@login_required
def site_remove(request, pk):
    deleted = None
    if request.method == 'POST':
        site = get_object_or_404(SiteData, pk=pk)
        deleted = f'Record with site id {site.site_id} is deleted successfully'
        context= {'deleted': deleted, 'site':site}
        #site.delete()
        return redirect('search')
    else:
        site = get_object_or_404(SiteData, pk=pk)
        context= {'deleted': deleted, 'site':site}
        return render(request, "ro_app/civil_main.html",context)

class SearchView(ListView):
    model = SiteData
    template_name = 'ro_app/civil_main.html'
    context_object_name = 'all_search_results'

class SiteDetailView(DetailView):
    model = SiteData
    template_name = 'ro_app/civil_main.html'
    context_object_name = 'site_details'

def autocomplete(request):
    if 'term' in request.GET:
        qs = SiteInfo.objects.filter(email_address__icontains=request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.append(product.email_address)
        return JsonResponse(titles, safe=False)
    return render(request, 'ro_app/civil_main.html')

@login_required
def modalview(request, pk = None):

    added = None
    edited = None
    cons_vals = ConsVals.objects.all()
    req_vals = ReqVals.objects.all()
    stat_vals = StatVals.objects.all()
    site_vals = SiteVals.objects.all()
    buil_vals = BuilVals.objects.all()
    act_vals = ActVals.objects.all()
    star_vals = StarVals.objects.all()

    if pk:
        inst = SiteData.objects.get(id=pk)
    else:
        inst = SiteData()

    if request.method == 'POST':

        inst.site_id= request.POST.get('site_id')
        inst.consultant_name = ConsVals.objects.get(consultant_name = request.POST.get('consultant_name'))
        inst.requester_dept = ReqVals.objects.get(requester_dept = request.POST.get('requester_dept'))

        #logic needs to be created for status
        inst.status = StatVals.objects.get(status = request.POST.get('status'))

        inst.site_case = SiteVals.objects.get(site_case = request.POST.get('site_case'))
        inst.building = BuilVals.objects.get(building = request.POST.get('building'))
        inst.action_taken = ActVals.objects.get(action_taken = request.POST.get('action_taken'))
        inst.star_site = StarVals.objects.get(star_site = request.POST.get('star_site'))
        inst.remarks= request.POST.get('Remarks')
        inst.mail_name= request.POST.get('mail_name')
        inst.project_name= request.POST.get('project_name')
        inst.new_requirement= request.POST.get('new_requirement')
        inst.request_date= request.POST.get('request_date')
        inst.last_visit= request.POST.get('last_visit')
        inst.feedback= request.POST.get('feedback')
        inst.max_rating_per= request.POST.get('max_rating_per')
        inst.email_address= request.POST.get('employee_email')
        inst.max_rating_in= 'ay7aga'
        inst.consultant_recommendations= 'ay7aga'

        # try:
        #     obj_filtered = SiteInfo.objects.get(email_address=str(request.POST.get('employee_email')))
        #     staff_id_value = getattr(obj_filtered, 'staff_id')
        # except ObjectDoesNotExist:
        #     staff_id_value = "NANA"
        # inst.staff_id= staff_id_value

        #Will be converted to servant app
        try:
            obj_filtered = SiteInfo.objects.get(site_id=request.POST.get('site_id'))
            area_value = getattr(obj_filtered, 'area')
            rt_gf_value = getattr(obj_filtered, 'rt_gf')
            str_type_value = getattr(obj_filtered, 'str_type')
            height_value = getattr(obj_filtered, 'height')
        except ObjectDoesNotExist:
            area_value = "NANA"
            rt_gf_value = "NANA"
            str_type_value = "NANA"
            height_value = "NANA"
        inst.area = area_value
        inst.rt_gf = rt_gf_value
        inst.str_type = str_type_value
        inst.height = height_value

        #logic needs to be created for status
        if str(request.POST.get('status')) == "Pending":
            inst.in_progress_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        elif str(request.POST.get('status')) == "Done":
            inst.done_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        inst.save()

        if pk:
            edited = f'Record with site id {inst.site_id} is edited successfully'
            context= {'cons_vals': cons_vals,'req_vals': req_vals,
            'stat_vals': stat_vals,'site_vals': site_vals,
            'buil_vals': buil_vals,'act_vals': act_vals,
            'star_vals': star_vals,'inst': inst,'edited': edited }
            return render(request, "ro_app/civil_main.html", context)

        else:
            added = f'Record with site id {inst.site_id} is created successfully'
            context= {'cons_vals': cons_vals,'req_vals': req_vals,
            'stat_vals': stat_vals,'site_vals': site_vals,
            'buil_vals': buil_vals,'act_vals': act_vals,
            'star_vals': star_vals,'inst': inst,'added': added }
            return render(request, "ro_app/civil_main.html", context)

    else:
        context= {'cons_vals': cons_vals,'req_vals': req_vals,
        'stat_vals': stat_vals,'site_vals': site_vals,
        'buil_vals': buil_vals,'act_vals': act_vals,
        'star_vals': star_vals,'inst': inst}
        return render(request, "ro_app/civil_main.html", context)