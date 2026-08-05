from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import CalculatorForm, LeadForm
from .pricing import calculate_price


def index(request):
    lead_form = LeadForm()
    calculator_form = CalculatorForm()
    price_range = None

    if request.method == "POST" and request.POST.get("form_name") == "lead":
        lead_form = LeadForm(request.POST)
        if lead_form.is_valid():
            lead_form.save()
            messages.success(
                request, "Заявка отправлена! Мы свяжемся с вами в ближайшее время."
            )
            return redirect(f"{reverse('home')}#contact-form")

    elif request.method == "POST" and request.POST.get("form_name") == "calculator":
        calculator_form = CalculatorForm(request.POST)
        if calculator_form.is_valid():
            price_range = calculate_price(
                calculator_form.cleaned_data["service"],
                calculator_form.cleaned_data["scenarios"],
                calculator_form.cleaned_data["integrations"],
            )

    return render(
        request,
        "landing/index.html",
        {
            "form": lead_form,
            "calculator_form": calculator_form,
            "price_range": price_range,
        },
    )
