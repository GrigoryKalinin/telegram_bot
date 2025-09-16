from django.db import models


class Sport(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Вид спорта")
    description = models.TextField(max_length=1000, verbose_name="Описание", blank=True)
    available = models.BooleanField(default=True, verbose_name="Доступность")
    
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
    district = models.ForeignKey('District', on_delete=models.CASCADE, verbose_name="Район")

    def __str__(self) -> str:
        return str(self.name)


class District(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Район")
    available = models.BooleanField(default=True, verbose_name="Доступность")

    def __str__(self) -> str:
        return str(self.name)


class SportPlace(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name="Цена", blank=True, null=True)
    is_paid = models.BooleanField(default=False, verbose_name="Платно")
    
    def __str__(self) -> str:
        return f"{self.sport} - {self.place}"


class CoachSportPlace(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    sport_place = models.ForeignKey(SportPlace, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.coach} - {self.sport_place}"