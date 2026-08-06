function initContactToggle() {
    const phoneInput = document.getElementById("phone-input");
    const telegramInput = document.getElementById("telegram-input");
    const hiddenContact = document.getElementById("id_contact");

    if (!phoneInput || !telegramInput || !hiddenContact) {
        return;
    }

    const toggleButtons = document.querySelectorAll(".contact-toggle-btn");
    const fields = document.querySelectorAll(".contact-field");

    let iti = null;
    if (window.intlTelInput) {
        try {
            iti = window.intlTelInput(phoneInput, {
                initialCountry: "ru",
                separateDialCode: true,
                uiTranslations: { searchPlaceholder: "Поиск страны" },
            });
        } catch (err) {
            console.error("intl-tel-input failed to initialize", err);
        }
    } else {
        console.error("intl-tel-input script did not load (window.intlTelInput is missing)");
    }

    let mode = "phone";

    function syncContact() {
        if (mode === "phone") {
            hiddenContact.value = (iti && iti.getNumber()) || phoneInput.value;
        } else {
            let value = telegramInput.value.trim();
            if (value && !value.startsWith("@")) {
                value = "@" + value;
            }
            hiddenContact.value = value;
        }
    }

    function setMode(newMode) {
        mode = newMode;
        toggleButtons.forEach(function (btn) {
            btn.classList.toggle("active", btn.dataset.mode === newMode);
        });
        fields.forEach(function (field) {
            field.hidden = field.dataset.field !== newMode;
        });
        syncContact();
    }

    toggleButtons.forEach(function (btn) {
        btn.addEventListener("click", function () {
            setMode(btn.dataset.mode);
        });
    });

    phoneInput.addEventListener("input", syncContact);
    telegramInput.addEventListener("input", syncContact);

    const existingValue = hiddenContact.value.trim();
    if (existingValue.startsWith("@")) {
        setMode("telegram");
        telegramInput.value = existingValue;
    } else if (existingValue && iti) {
        setMode("phone");
        iti.setNumber(existingValue);
    }

    syncContact();
}

document.addEventListener("DOMContentLoaded", initContactToggle);
document.body.addEventListener("htmx:afterSwap", initContactToggle);
