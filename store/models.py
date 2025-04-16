from djongo import models  # Ensure you're importing from djongo

class Product(models.Model):
    id = models.ObjectIdField()  # Djongo-specific field
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name
