from django.shortcuts import render
from django.http import Http404

from .models import Promo, Teacher


# Create your views here.
def index(request):
    teachers_list = Teacher.objects.order_by("-id")[:20]
    context = {"teachers_list": teachers_list}
    return render(request, "teachers/index.html", context)


def view_teacher(request, teacher_id):
    try:
        teacher = Teacher.objects.get(pk=teacher_id)
    except Teacher.DoesNotExist:
        raise Http404("Teacher not found")
    return render(request, "teachers/view.html", {'teacher': teacher})


def promo(request):
    promos_list = Promo.objects.order_by("-id")[:20]
    context = {"promos_list": promos_list}
    return render(request, "promos/index.html", context)


def view_promo(request, promo_id):
    try:
        promo = Promo.objects.get(pk=promo_id)
    except Promo.DoesNotExist:
        raise Http404("Teacher not found")
    return render(request, "promos/view.html", {'promo': promo})

