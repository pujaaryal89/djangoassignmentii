from django.db import models
from django.contrib.auth.models import User,Group
# Create your models here.

class Blog(models.Model):
	title=models.CharField(max_length=50)
	description=models.TextField()
	author=models.ForeignKey('Author',on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	image=models.ImageField(upload_to='blog',null=True,blank=True)

	def __str__(self):
		return self.title


class Author(models.Model):
	name=models.CharField(max_length=50)
	visitor=models.OneToOneField('Visitor',on_delete=models.CASCADE)
	email=models.EmailField()
	phone=models.CharField(max_length=50)


	def __str__(self):
		return self.name

class Visitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to='visitors', null=True, blank=True)



    def save(self, *args, **kwargs):
        grp, created = Group.objects.get_or_create(name='visitor')
        self.user.groups.add(grp)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name		