from django.db import models


DIVISIONS = (('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'))

# Creating a db model


class People(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    standard = models.IntegerField()
    division = models.CharField(
        choices=DIVISIONS, default='A', max_length=1)
    school = models.CharField(max_length=100)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey('auth.User', related_name='people', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']
    
    def save(self, *args, **kwargs):
        super(People, self).save(*args, **kwargs)
