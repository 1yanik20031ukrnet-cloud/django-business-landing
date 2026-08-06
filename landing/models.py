from django.db import models


class Lead(models.Model):
    class Service(models.TextChoices):
        BASIC_BOT = "basic", "Базовый бот"
        BOT_WITH_DB = "bot_db", "Бот + база данных"
        AI_AGENT = "ai_agent", "AI-агент"

    class Status(models.TextChoices):
        NEW = "new", "Новая"
        CONTACTED = "contacted", "Связались"
        IN_PROGRESS = "in_progress", "В работе"
        DONE = "done", "Выполнена"
        CANCELLED = "cancelled", "Отменена"

    name = models.CharField("Имя", max_length=100)
    contact = models.CharField("Telegram или телефон", max_length=100)
    service = models.CharField(
        "Услуга", max_length=20, choices=Service.choices, default=Service.BASIC_BOT
    )
    message = models.TextField("Сообщение", max_length=1000, blank=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    status = models.CharField(
        "Статус", max_length=20, choices=Status.choices, default=Status.NEW
    )

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.get_service_display()}"
