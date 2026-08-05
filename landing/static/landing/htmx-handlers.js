document.body.addEventListener("htmx:responseError", function (evt) {
    if (evt.detail.target && evt.detail.target.id === "calculator-result") {
        evt.detail.target.innerHTML =
            '<div class="calculator-result calculator-error">Не получилось рассчитать стоимость. Попробуйте ещё раз.</div>';
    }
});

document.body.addEventListener("htmx:sendError", function (evt) {
    if (evt.detail.target && evt.detail.target.id === "calculator-result") {
        evt.detail.target.innerHTML =
            '<div class="calculator-result calculator-error">Нет соединения с сервером. Проверьте интернет и попробуйте снова.</div>';
    }
});
