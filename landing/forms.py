import re

from django import forms

from .models import Lead

USERNAME_RE = re.compile(r"[A-Za-z0-9_]{5,32}$")
PHONE_RE = re.compile(r"\+?\d{10,15}$")


class LeadForm(forms.ModelForm):
    contact = forms.CharField(widget=forms.HiddenInput(), max_length=100)

    class Meta:
        model = Lead
        fields = ["name", "contact", "service", "message"]

    def clean_name(self):
        return self.cleaned_data["name"].strip()

    def clean_contact(self):
        contact = self.cleaned_data["contact"].strip()

        if contact.startswith("@"):
            username = contact[1:]
            if not USERNAME_RE.fullmatch(username):
                raise forms.ValidationError(
                    "Похоже на Telegram-юзернейм, но формат неверный: "
                    "только латинские буквы, цифры и _, от 5 до 32 символов."
                )
            return "@" + username

        digits = re.sub(r"[^\d+]", "", contact)
        if PHONE_RE.fullmatch(digits):
            if not digits.startswith("+"):
                digits = "+" + digits
            return digits

        raise forms.ValidationError(
            "Укажите номер телефона (например +79991234567) "
            "или Telegram-юзернейм, начинающийся с @."
        )


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
