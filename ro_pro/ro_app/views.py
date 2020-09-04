from django.shortcuts import render , get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from ro_app.models import ConsVals,ReqVals,StatVals,SiteVals,BuilVals,ActVals,StarVals,SiteData, SiteInfo
from django.http import JsonResponse, HttpResponse
import json
from django.contrib import messages

def autocomplete(request):
    if 'term' in request.GET:
        qs = SiteInfo.objects.filter(email_address__icontains=request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.append(product.email_address)
        return JsonResponse(titles, safe=False)
    return render(request, 'ro_app/civil_main.html')

@login_required
def civil_fn(request, pk = None):

    if '/roapp/search/' in request.path:
        search_data = SiteData.objects.all()
        context= {'all_search_results': search_data}
        return render(request, "ro_app/civil_main.html", context)
        
    cons_vals = ConsVals.objects.all()
    req_vals = ReqVals.objects.all()
    stat_vals = StatVals.objects.all()
    site_vals = SiteVals.objects.all()
    buil_vals = BuilVals.objects.all()
    act_vals = ActVals.objects.all()
    star_vals = StarVals.objects.all()

    if pk:
        civil_request = SiteData.objects.get(id=pk)
    else:
        civil_request = SiteData()

    if request.method == 'POST' and 'delete_modal_button' in request.POST:
        #civil_request.delete()
        messages.error(request, "Deleted Successfully!")
        return redirect('search')

    if request.method == 'POST' and 'edit_add_modal_button' in request.POST:

        civil_request.site_id= request.POST.get('site_id')
        civil_request.consultant_name = ConsVals.objects.get(consultant_name = request.POST.get('consultant_name'))
        civil_request.requester_dept = ReqVals.objects.get(requester_dept = request.POST.get('requester_dept'))

        #logic needs to be created for status
        civil_request.status = StatVals.objects.get(status = request.POST.get('status'))

        civil_request.site_case = SiteVals.objects.get(site_case = request.POST.get('site_case'))
        civil_request.building = BuilVals.objects.get(building = request.POST.get('building'))
        civil_request.action_taken = ActVals.objects.get(action_taken = request.POST.get('action_taken'))
        civil_request.star_site = StarVals.objects.get(star_site = request.POST.get('star_site'))
        civil_request.remarks= request.POST.get('Remarks')
        civil_request.mail_name= request.POST.get('mail_name')
        civil_request.project_name= request.POST.get('project_name')
        civil_request.new_requirement= request.POST.get('new_requirement')
        civil_request.request_date= request.POST.get('request_date')
        civil_request.last_visit= request.POST.get('last_visit')
        civil_request.feedback= request.POST.get('feedback')
        civil_request.max_rating_per= request.POST.get('max_rating_per')
        civil_request.email_address= request.POST.get('employee_email')
        civil_request.max_rating_in= 'ay7aga'
        civil_request.consultant_recommendations= 'ay7aga'

        # try:
        #     obj_filtered = SiteInfo.objects.get(email_address=str(request.POST.get('employee_email')))
        #     staff_id_value = getattr(obj_filtered, 'staff_id')
        # except ObjectDoesNotExist:
        #     staff_id_value = "NANA"
        # civil_request.staff_id= staff_id_value

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
        civil_request.area = area_value
        civil_request.rt_gf = rt_gf_value
        civil_request.str_type = str_type_value
        civil_request.height = height_value

        #logic needs to be created for status
        if str(request.POST.get('status')) == "Pending":
            civil_request.in_progress_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        elif str(request.POST.get('status')) == "Done":
            civil_request.done_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        civil_request.save()

        if pk:
            messages.success(request, "Edited Successfully!")
            return redirect('search')

        else:
            messages.success(request, "Added Successfully!")
            return redirect('search')

    else:
        context= {'cons_vals': cons_vals,'req_vals': req_vals,
        'stat_vals': stat_vals,'site_vals': site_vals,
        'buil_vals': buil_vals,'act_vals': act_vals,
        'star_vals': star_vals,'civil_request': civil_request}
        return render(request, "ro_app/civil_main.html", context)