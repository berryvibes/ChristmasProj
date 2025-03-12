from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
from christmasApp.models import Product
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from christmasApp.models import Product




# Create your views here.



def send_email(request):
    # Check if the user is authenticated and has a 'seller' user_type in their profile
    if request.user.is_authenticated and hasattr(request.user, 'profile') and request.user.profile.user_type == 'seller':
        if request.method == "POST":
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            recipient_email = request.POST.get('recipient_email')

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [recipient_email],
                fail_silently=False,
            )
            return HttpResponse("Email sent successfully.")
        else:
            return render(request, "user/send_email.html")
    else:
        return HttpResponse("Unauthorized", status=403)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login') # Redirect to login after successful registration
        else:
            messages.error(request, 'Please correct the errors below.')  # Provide feedback for form errors
    else:
        form = RegistrationForm()
    return render(request, 'user/register.html', {'form': form})



@login_required
def profile(request):
    profile = request.user.profile
    context = {'profile': profile}
    
    # Check if the user is a seller
    # Check if the user is a seller
    if profile.user_type == 'seller':
        products = Product.objects.filter(user=request.user)
        context['products'] = products
        

        return render(request, 'user/seller_profile.html', context)
    else:
        return render(request, 'user/profile.html', context)
    

@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            request.user.refresh_from_db()  
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'user/edit_profile.html', {'form': form})


@login_required
def buyer_dashboard(request):
    return render(request, 'user/buyer_dashboard.html')



@login_required
def seller_dashboard(request):
    return render(request, 'user/seller_dashboard.html')