from django.db import models


class Sport(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Вид спорта")
    description = models.TextField(max_length=1000, verbose_name="Описание", blank=True)
    available = models.BooleanField(default=True, verbose_name="Доступность")
    is_paid = models.BooleanField(default=False, verbose_name="Платно")
    price = models.IntegerField(verbose_name="Цена", blank=True, null=True)

    coach = models.ManyToManyField("Coach", verbose_name="Тренер", blank=True)
    place = models.ManyToManyField("Place", verbose_name="Место", blank=True)
    district = models.ManyToManyField("District", verbose_name="Район", blank=True)

    def __str__(self) -> str:
        return str(self.name)


class Coach(models.Model):
    first_name = models.CharField(max_length=100, db_index=True, verbose_name="Имя")
    last_name = models.CharField(max_length=100, db_index=True, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=100, db_index=True, verbose_name="Отчество")
    description = models.TextField(max_length=1000, verbose_name="Описание", blank=True)
    available = models.BooleanField(default=True, verbose_name="Доступность")
    phone = models.CharField(max_length=12, verbose_name="Телефон", blank=True)

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name} {self.middle_name}"


class Place(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Место")
    description = models.TextField(max_length=1000, verbose_name="Описание", blank=True)
    available = models.BooleanField(default=True, verbose_name="Доступность")

    coach = models.ManyToManyField(Coach, verbose_name="Тренер", blank=True)

    def __str__(self) -> str:
        return str(self.name)


class District(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Район")
    available = models.BooleanField(default=True, verbose_name="Доступность")

    place = models.ForeignKey(Place, verbose_name="Место", on_delete=models.CASCADE)
    coach = models.ManyToManyField(Coach, verbose_name="Тренер", blank=True)

    def __str__(self) -> str:
        return str(self.name)
