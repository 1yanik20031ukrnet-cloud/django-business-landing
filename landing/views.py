from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LeadForm


def index(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Заявка отправлена! Мы свяжемся с вами в ближайшее время."
            )
            return redirect(f"{reverse('home')}#contact-form")
    else:
        form = LeadForm()

    return render(request, "landing/index.html", {"form": form})
