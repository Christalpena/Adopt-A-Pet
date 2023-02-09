from django.db import models

# Create your models here.

class Race(models.Model):
    race = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Race'
        verbose_name_plural = 'Races'

    def __str__(self):
        return self.race
        
class KindOfPet(models.Model):
    kind = models.CharField(max_length=50, verbose_name='Kind of Pet')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'KindOfPet'
        verbose_name_plural = 'KindOfPets'

    def __str__(self):
        return self.kind


class Animal(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    height = models.FloatField(blank=True)
    vaccines = models.BooleanField(blank=True)
    photo = models.ImageField(upload_to='AdopImages')
    description = models.CharField(max_length=1000)
    age = models.IntegerField()
    birth_date = models.DateField(verbose_name='date of birth')
    race = models.ForeignKey(Race,on_delete=models.CASCADE)
    kind = models.ForeignKey(KindOfPet,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animals'

    def __str__(self):
        return self.name

class PersonInformation(models.Model):
    animal_name = models.CharField(max_length=30)
    animal_id = models.IntegerField()
    person_name = models.CharField(max_length=30)
    person_last_name = models.CharField(max_length=50)
    id_number = models.IntegerField()
    date_of_birth = models.DateField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    civil_status = models.CharField(max_length=10)
    profession = models.CharField(max_length=60)
    phone = models.IntegerField()
    gmail = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'PersonInformation'
        verbose_name_plural = 'PersonInformations'

    def __str__(self):
        return self.person_name