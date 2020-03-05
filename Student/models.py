from django.db import models

class Student(models.Model):
	stu_name = models.CharField(max_length=200,db_index=True)
	email=models.EmailField()
	stu_father_name = models.CharField(max_length=200)
	stu_mother_name = models.CharField(max_length=200)
	stu_father_occupation = models.CharField(max_length=100)
	stu_mother_occupation = models.CharField(max_length=100)
	stu_father_mobilenumber = models.BigIntegerField()
	stu_mother_mobilenumber = models.BigIntegerField()
	stu_class = models.CharField(max_length=150)
	stu_batch = models.CharField(max_length=150)
	stu_gender = models.CharField(max_length=120)

	def __str__(self):
		return 'Student {}'.format(self.id)
