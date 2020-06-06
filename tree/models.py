import uuid
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.
class Tree(models.Model):
	id     =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name    =   models.CharField(max_length=100)
	nickname = models.CharField(max_length=50, blank=True, null=True)
	details =   models.CharField(max_length=500)
	image   =   models.URLField(default='https://image.flaticon.com/icons/png/512/861/861086.png')
	family  =   models.CharField(max_length=50, blank=True, null=True)
	lat     =   models.CharField(max_length=100, blank=True, null=True)
	lng     =   models.CharField(max_length=100, blank=True, null=True)
	owner   =   models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	broken = models.BooleanField(default=False)
	approved = models.BooleanField(default=False)


	def __str__(self):
		return f'{self.id}'

	def get_absolute_url(self):
		return reverse('tree:detail', kwargs={"id": self.id })

	class Meta:
		verbose_name_plural = "Trees Planted by User"