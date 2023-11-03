from django.db import models

# Create your models here.
class Article(models.Model):
    NAPEDY = [
        ('przedninaped', 'Przedni napęd'),
        ('tylnaped', 'Tylni naped'),
        ('4x4', "Napęd 4x4"),
    ]

    marka = models.CharField(max_length=30, blank=False, unique=False)
    model = models.CharField(max_length=30, blank=False, unique=False)
    silnik = models.CharField(max_length=10, blank=False, unique=False)
    skrzynia_biegów = models.CharField(max_length=20, blank=False, unique=False)
    drzwi = models.IntegerField(blank=False, unique=False)
    rok = models.PositiveSmallIntegerField(default=2023)
    naped = models.CharField(max_length=20, choices=NAPEDY, blank=False, unique=False)

    def __str__(self):
        return self.marka + self.model + self.silnik + self.skrzynia_biegów + self.drzwi + self.rok + self.naped