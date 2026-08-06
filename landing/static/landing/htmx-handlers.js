window.addEventListener("load", function () {
    document.documentElement.style.scrollBehavior = "smooth";
});

function showRequestError(evt, message) {
    const target = evt.detail.target;
    if (!target) {
        return;
    }

    if (target.id === "calculator-result") {
        target.innerHTML = '<div class="calculator-result calculator-error">' + message + "</div>";
    } else if (target.id === "lead-form-wrap") {
        let box = target.querySelector(".form-error-box");
        if (!box) {
            box = document.createElement("p");
            box.className = "form-error form-error-box";
            target.prepend(box);
        }
        box.textContent = message;

        const submitBtn = target.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.disabled = false;
        }
    }
}

document.body.addEventListener("htmx:responseError", function (evt) {
    showRequestError(evt, "Не получилось отправить запрос. Попробуйте ещё раз.");
});

document.body.addEventListener("htmx:sendError", function (evt) {
    showRequestError(evt, "Нет соединения с сервером. Проверьте интернет и попробуйте снова.");
});
