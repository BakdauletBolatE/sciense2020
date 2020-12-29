from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model):
    name = models.CharField("Сабақтың аты",max_length=255)

    class Meta:
        verbose_name = "Пән"
        verbose_name_plural = "Пәндер"

    def __str__(self):
        return self.name

class GrantHolders(models.Model):
    name = models.CharField("Грант иегерінің есімі", max_length=200)
    age = models.DateField("Туылған жылы")
    poster = models.ImageField("Грант иегерінің суреті",upload_to="graduate_img/")
    teacher = models.CharField("Ғылыми жетекшісі",max_length=200)
    bachelor = "Бакалавр"
    magistracy = "Магистратура"
    doctoralstudies = "Доктарантура"
    DEGREE_CHOICES = [
        (bachelor, 'Бакалавр'),
        (magistracy, 'Магистратура'),
        (doctoralstudies, 'Доктарантура'),
    ]
    degree = models.CharField(
        max_length=30,
        choices=DEGREE_CHOICES,
        default=bachelor
    )
    slug = models.SlugField("url",unique=True)
    project_name = models.CharField("Жобаның тақырыбы",max_length=255)
    project_duration = models.CharField("Жобаның мерзімі",max_length=255)
    purpose_project = models.CharField("Жобаның мақсаты",max_length=255)
    ways_project = models.TextField("Жоба мақсатына жету жолдары")
    expected_result = models.TextField("Күтілетін нәтиже")
    novelty_scientific = models.TextField("Ғылыми жұмыстың жаңалығы")
    graduate_year = models.IntegerField("Грант алған жылы",default=0) 
    subject = models.ForeignKey(Subject,verbose_name="Грант иегерінің пәні",on_delete=models.CASCADE,blank=True,null=True)
     
    class Meta:
        verbose_name = "Грант иегері"
        verbose_name_plural = "Грант иегерлері"

    def __str__(self):
        return self.name
        
class Like(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(GrantHolders,on_delete=models.CASCADE)
    
    