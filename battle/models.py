from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from monster.models import Monster


# Create your models here.
class Battle(models.Model):
    monsterA = models.ForeignKey(Monster, related_name='battlesA', on_delete=models.PROTECT)

    monsterB = models.ForeignKey(Monster, related_name='battlesB', on_delete=models.PROTECT)

    winner = models.PositiveSmallIntegerField(
        blank=False,
        verbose_name="Winner",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    def start(self):
        self.winner = 2345
        self.save()

    class Meta:
        verbose_name = "Battle"
        verbose_name_plural = "Battles"
        ordering = ["id"]
