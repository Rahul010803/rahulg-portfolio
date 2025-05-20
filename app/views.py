from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.http import JsonResponse

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send email
            send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                [settings.EMAIL_RECIPIENT],  
                fail_silently=False,
            )
            # Return JSON response
            return JsonResponse({'success': True, 'message': 'Your message has been sent. Thank you!'})
        else:
            # Return JSON response with error message
            return JsonResponse({'success': False, 'message': 'There was an error with your submission.'})
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})
