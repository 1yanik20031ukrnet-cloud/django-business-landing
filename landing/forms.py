from django import forms

from .models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ["name", "contact", "service", "message"]


class CalculatorForm(forms.Form):
    SCENARIOS_CHOICES = [
        ("1-3", "1–3 сценария"),
        ("4-7", "4–7 сценариев"),
        ("8+", "8+ сценариев"),
    ]

    service = forms.ChoiceField(label="Тип бота", choices=Lead.Service.choices)
    scenarios = forms.ChoiceField(
        label="Сколько сценариев диалога", choices=SCENARIOS_CHOICES
    )
    integrations = forms.BooleanField(
        label="Нужны интеграции (CRM, оплата и т.п.)", required=False
    )
