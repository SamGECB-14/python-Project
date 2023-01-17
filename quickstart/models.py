from django.db import models

class employee(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.firstname
class Student(models.Model):
    name = models.CharField(max_length=50)
    rol_number = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Singer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    photo = photo=models.FileField(upload_to='SingerImages/',null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']



class Song(models.Model):
    singer= models.ForeignKey(Singer, related_name='song', on_delete=models.CASCADE,default = "")
    name = models.CharField('Song Name',max_length=50)
    release_date = models.DateField()

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
