
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth import logout

from .forms import MedicineForm
from .models import Medicine
from django.core.paginator import Paginator
from django.shortcuts import render, redirect 



def home(request):
    if not request.user.is_authenticated:
        return redirect('signup')
    return render(request, 'home.html')

def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('retrieveproduct')
        
    else:
            form = AuthenticationForm()
            
    return render(request, 'login.html', {'form': form})

@login_required(login_url='/login/')
def logout_page(request):
    
    if request.method == 'POST':
        logout(request)
        
        return redirect('login')
    return render(request, 'logout.html')


@login_required(login_url='/login/')
def create_medicine(request):
    if Medicine.objects.filter(user=request.user).count() >= 5:
        return render(request, 'create.html', {
            'error': "You cannot add more than 5 medicines.",
            'form': MedicineForm()
        })
    
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            medicine = form.save(commit=False)
            medicine.user = request.user
            medicine.save()
            return redirect('retrieveproduct')
    else:
        form = MedicineForm()
        
    return render(request, 'create.html', {'form': form})
        
@login_required(login_url='/login/')
def retrieve_medicine(request):
    product_list = Medicine.objects.filter(user=request.user).order_by('-added_time')
    paginator = Paginator(product_list, 3)  # 3 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'retrieve.html', {'page_obj': page_obj})
    


@login_required(login_url='/login/')
def update_medicine(request, id):
    product = Medicine.objects.get(pk=id)
    
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('retrieveproduct')
        
    else:
            form = MedicineForm(instance=product)
            
    return render(request, 'update.html', {'form': form})


@login_required(login_url='/login/')
def delete_medicine(request, id):
    product = Medicine.objects.get(pk=id)
    
    
    if request.method == 'POST':
        product.delete()
        return redirect('retrieveproduct')
    
    
    return render(request, 'delete.html', {'product': product})


def listing(request):
    products = Medicine.objects.filter(user=request.user).order_by('-added_time')
    paginator = Paginator(products, 3)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    return render(request, 'pagination.html', {'page_obj': page_obj})


@login_required(login_url='/login/')
def search_medicine(request):
    results = []
    if 'search_term' in request.GET:
        search_term = request.GET['search_term']
        results = Medicine.objects.filter(
            user=request.user,
            name__icontains=search_term
        )
    return render(request, "search.html", {"results": results})


            
    
    
    
    
    

