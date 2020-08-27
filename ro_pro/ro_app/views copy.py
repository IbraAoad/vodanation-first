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



var_add_view = False
var_detail_view = False
var_remove_view = False
var_edit_view = False
var_searchview = False






def modalview(request):

    cons_vals = ConsVals.objects.all()
    req_vals = ReqVals.objects.all()
    stat_vals = StatVals.objects.all()
    site_vals = SiteVals.objects.all()
    buil_vals = BuilVals.objects.all()
    act_vals = ActVals.objects.all()
    star_vals = StarVals.objects.all()

    if request.method == 'POST':
        inst=SiteData()
        inst.site_id= request.POST.get('site_id')

        conso_submitted = request.POST.get('consultant_name')
        inst.consultant_name = ConsVals.objects.get(consultant_name = conso_submitted)

        req_submitted = request.POST.get('requester_dept')
        inst.requester_dept = ReqVals.objects.get(requester_dept = req_submitted)

        status_submitted = request.POST.get('status')
        inst.status = StatVals.objects.get(status = status_submitted)

        site_submitted = request.POST.get('site_case')
        inst.site_case = SiteVals.objects.get(site_case = site_submitted)

        buil_submitted = request.POST.get('building')
        inst.building = BuilVals.objects.get(building = buil_submitted)

        act_submitted = request.POST.get('action_taken')
        inst.action_taken = ActVals.objects.get(action_taken = act_submitted)

        star_submitted = request.POST.get('star_site')
        inst.star_site = StarVals.objects.get(star_site = star_submitted)

        inst.remarks= request.POST.get('Remarks')
        inst.mail_name= request.POST.get('mail_name')
        inst.project_name= request.POST.get('project_name')
        inst.new_requirement= request.POST.get('new_requirement')
        inst.request_date= request.POST.get('request_date')
        inst.last_visit= request.POST.get('last_visit')
        inst.feedback= request.POST.get('feedback')
        inst.max_rating_per= request.POST.get('max_rating_per')
        inst.employee_email= request.POST.get('employee_email')

        inst.area= 'ay7aga'
        inst.rt_gf= 'ay7aga'
        inst.str_type= 'ay7aga'
        inst.height= 'ay7aga'
        inst.max_rating_in= 'ay7aga'
        inst.consultant_recommendations= 'ay7aga'
        inst.height= 'ay7aga'
        inst.height= 'ay7aga'
        inst.save()
        
        context= {'cons_vals': cons_vals,'req_vals': req_vals,
        'stat_vals': stat_vals,'site_vals': site_vals,
        'buil_vals': buil_vals,'act_vals': act_vals,
        'star_vals': star_vals,}
        return render(request, "ro_app/ro_main.html", context)
    else:
        context= {'cons_vals': cons_vals,'req_vals': req_vals,
        'stat_vals': stat_vals,'site_vals': site_vals,
        'buil_vals': buil_vals,'act_vals': act_vals,
        'star_vals': star_vals,}
        return render(request, "ro_app/ro_main.html", context)