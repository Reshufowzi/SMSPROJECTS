from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name


class Placementcell(models.Model):
    student_name = models.CharField(max_length=50)
    student_image = models.ImageField(upload_to='placementcell')
    dep_name = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name+ " : " +str(self.dep_name)

class Search(models.Model):
    student_name = models.CharField(max_length=50)
    student_phonenumber = models.CharField(max_length=10)
    student_email = models.EmailField()
    student_image = models.ForeignKey(Placementcell,on_delete=models.CASCADE)
