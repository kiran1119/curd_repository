from django.shortcuts import render
from .models import ProductData
from .forms import InsertingDataForm, UpdatingDataForm,DeletingDataForm
from django.http.response import HttpResponse


def main_view(request):
    return render(request, 'main.html')


def insert_view(request):
    if request.method == 'POST':
        pform = InsertingDataForm(request.POST)
        if pform.is_valid():
            product_id = request.POST.get('product_id', '')
            product_name = request.POST.get('product_name', '')
            product_cost = request.POST.get('product_cost', '')
            product_color = request.POST.get('product_color', '')
            product_class = request.POST.get('product_class', '')
            customer_name = request.POST.get('customer_name', '')
            customer_mobile = request.POST.get('customer_mobile', '')
            customer_email = request.POST.get('customer_email', '')

            data = ProductData(
                product_id=product_id,
                product_name=product_name,
                product_cost=product_cost,
                product_class=product_class,
                product_color=product_color,
                customer_name=customer_name,
                customer_mobile=customer_mobile,
                customer_email=customer_email
            )
            data.save()
            pform = InsertingDataForm()
            return render(request, 'insert.html', {'pform': pform})
        else:
            return HttpResponse('Invalid data')
    else:
        pform = InsertingDataForm
        return render(request, 'insert.html', {'pform': pform})


def retrieve_view(request):
    data = ProductData.objects.all()
    return render(request, 'retrieve.html', {'data': data})


def update_view(request):
    if request.method == 'POST':
        uform = UpdatingDataForm(request.POST)
        if uform.is_valid():
            product_id = request.POST.get('product_id', '')
            product_cost = request.POST.get('product_cost', '')
            pid = ProductData.objects.filter(product_id=product_id)
            if not pid:
                return HttpResponse('Invalid Product id')
            else:
                pid.update(product_cost=product_cost)
                uform = UpdatingDataForm()
                return render(request, 'update.html', {'uform':uform})
        else:
            return HttpResponse('Invalid product details ')

    else:
        uform = UpdatingDataForm()
        return render(request, 'update.html', {'uform': uform})


def delete_view(request):
    if request.method == 'POST':
        dform = DeletingDataForm(request.POST)
        product_id = request.POST.get('product_id', '')
        pid = ProductData.objects.filter(product_id=product_id)
        if not pid:
            return HttpResponse('Invalid product_id')
        else:
            pid.delete()
            dform = DeletingDataForm()
            return render(request, 'delete.html', {'dform':dform})


    else:
        dform = DeletingDataForm()
        return render(request, 'delete.html', {'dform':dform})
