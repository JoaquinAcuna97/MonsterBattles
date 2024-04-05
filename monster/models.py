from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, URLValidator


# Create your models here.
class Monster(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name",  default="A monster")
    speed = models.PositiveSmallIntegerField(
        blank=False,
        verbose_name="Speed",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    attack = models.PositiveSmallIntegerField(
        blank=False,
        verbose_name="Attack",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    defense = models.PositiveSmallIntegerField(
        blank=False,
        verbose_name="Defense",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    hp = models.PositiveSmallIntegerField(
        blank=False,
        verbose_name="Hp",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    imageUrl = models.URLField(
        max_length=200, verbose_name="Image URL", validators=[URLValidator()]
    )

    class Meta:
        verbose_name = "Monster"
        verbose_name_plural = "Monsters"
        ordering = ["name", "-attack"]

    def __str__(self):
        return f"{self.name}"
