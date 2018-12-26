from django.db import models

# Create your models here.


class Customer(models.Model):
    """Model representing an customer."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    Zip = models.CharField(max_length=10)

    class Meta:
        ordering = ['last_name', 'first_name']
    
    def get_absolute_url(self):
        """Returns the url to access a particular customer instance."""
        return reverse('customer-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
