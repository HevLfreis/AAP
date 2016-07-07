#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create your views here.

import json
import os

from django.http import HttpResponse
from django.template import Context
from django.shortcuts import *
from django.views.decorators.csrf import csrf_exempt

from table.models import Result, Main, Mainshow
from table.methods import perm_top, ad, minsdk, obf, handle_uploaded_file, userApk_handle


def detail(request):
    a = Main.objects.latest('id').id

    j = json.dumps([a])

    return HttpResponse(j)


def send_data_permission(request):
    r = Result.objects.get(id=1)

    j = json.dumps(perm_top(r.permission_num_str))

    return HttpResponse(j)


def send_data_ad(request):
    r = Result.objects.get(id=1)

    j = json.dumps(ad(r.ad_count_str))

    return HttpResponse(j)


def send_data_minsdk(request):
    r = Result.objects.get(id=1)

    j = json.dumps(minsdk(r.minsdk_count_str))

    return HttpResponse(j)


def send_data_obf(request):
    r = Result.objects.get(id=1)

    j = json.dumps(obf(r.obf_count_str))

    return HttpResponse(j)


####################################################################


def demo(request):
    # p = get_object_or_404(Main, md5=md5)
    r = Result.objects.get(id=1)

    context = Context()
    return HttpResponse(r.permission_num_str)


def redirect2main(request):
    # print(request.get_host())
    return HttpResponseRedirect('/main')


def index(request):
    context = Context()
    # print os.path.dirname(__file__)
    return render(request, 'table/index.html', context)


def index_p(request):
    context = Context()
    return render(request, 'table/index_p.html', context)


def index_o(request):
    context = Context()
    return render(request, 'table/index_o.html', context)


def index_a(request):
    context = Context()
    return render(request, 'table/index_a.html', context)


def index_m(request):
    context = Context()
    return render(request, 'table/index_m.html', context)


#######################################################################


def uploadify(request):
    return render_to_response()


@csrf_exempt
def uploader(request):
    file_obj = request.FILES['Filedata']
    r = handle_uploaded_file(file_obj)
    try:
        Main.objects.get(md5=r[1])
    except Main.DoesNotExist:
        status = userApk_handle(r[0])
        if status == 0:
            return HttpResponse(r[1])
        else:
            raise Http404
    else:
        return HttpResponse(r[1])


#######################################################################

def loading(request, md5):
    context = Context()
    return render(request, 'table/loading.html', context)


def show(request, md5):
    obj = get_object_or_404(Main, md5=md5)
    s = Mainshow(obj.packagename, obj.app_version, obj.md5, obj.permission_num_str, obj.risk, obj.minSDKversion,
                 obj.ad_SDK,
                 obj.CRYPTO, obj.DYNAMIC, obj.NATIVE, obj.REFLECTION)
    return render(request, 'table/show.html', {'app': s})
