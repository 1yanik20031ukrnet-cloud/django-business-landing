from datetime import timedelta

from django.shortcuts import render
from django.utils import timezone

from .forms import CalculatorForm, LeadForm
from .models import Lead
from .notifications import send_telegram_notification
from .pricing import calculate_price

DUPLICATE_WINDOW = timedelta(seconds=30)


def index(request):
    return render(
        request,
        "landing/index.html",
        {
            "form": LeadForm(),
            "calculator_form": CalculatorForm(),
            "price_range": None,
        },
    )


def submit_lead(request):
    lead_form = LeadForm(request.POST)
    success = False

    if lead_form.is_valid():
        is_duplicate = Lead.objects.filter(
            name=lead_form.cleaned_data["name"],
            contact=lead_form.cleaned_data["contact"],
            created_at__gte=timezone.now() - DUPLICATE_WINDOW,
        ).exists()

        if not is_duplicate:
            lead = lead_form.save()
            send_telegram_notification(lead)

        success = True
        lead_form = LeadForm()

    return render(
        request, "landing/partials/lead_form.html", {"form": lead_form, "success": success}
    )


def calculate(request):
    price_range = None
    calculator_form = CalculatorForm(request.POST)
    if calculator_form.is_valid():
        price_range = calculate_price(
            calculator_form.cleaned_data["service"],
            calculator_form.cleaned_data["scenarios"],
            calculator_form.cleaned_data["integrations"],
        )

    return render(
        request, "landing/partials/calculator_result.html", {"price_range": price_range}
    )
