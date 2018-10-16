from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from sekolah_kita_server.apps.province.models import Province
from sekolah_kita_server.core.decorators import user_staff_required
from sekolah_kita_server.apps.province.form import ProvinceForm


@user_staff_required
def index(request):
    provinces = Province.objects.order_by('id').all()
    page = request.GET.get('page', 1)

    paginator = Paginator(provinces, 20)
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_page)

    context_data = {
        'title': 'Provinsi',
        'page': page
    }
    return render(request, 'backoffice/province/index.html', context_data)


def details(request, id):
    province = get_object_or_404(Province.objects.all(), id=id)
    context_data = {
        'province': province,
    }
    return render(request, 'backoffice/province/details.html', context_data)


def add_province(request):
    form = ProvinceForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('backoffice:province:index')
    else:
        form = ProvinceForm()
    context_data = {
        'form': form
    }
    return render(request, 'backoffice/province/province_form.html',context_data)


def edit_province(request, id):
    province = get_object_or_404(Province.objects.all(), id=id)
    if request.method == "POST":
        form = ProvinceForm(request.POST or None, request.FILES or None, instance=province)
        if form.is_valid():
            province = form.save(commit=False)
            province.save()
            return redirect('backoffice:province:index')
    else:
        form = ProvinceForm(instance=province)
    context_data = {
        'form': form,
    }        
    return render(request, 'backoffice/province/province_form.html', context_data)