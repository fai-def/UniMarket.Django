from django.db import models
from django.contrib.auth.models import User # Required for linking products to students

class Product(models.Model):
    """
    Model representing an item listed in the university marketplace.
    Tracks product details, pricing, and ownership.
    """
    
    # Relationship: Each product belongs to a student (seller)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    
    # Core item details
    name = models.CharField(max_length=100, verbose_name="Item Name")
    description = models.TextField(verbose_name="Item Description")
    
    # Financial data: DecimalField is used for financial precision in Fintech systems
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    
    # Metadata for tracking and sorting
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Category and image (optional but recommended for a real marketplace)
    # category = models.CharField(max_length=50, blank=True)
    # image = models.ImageField(upload_to='products/', blank=True, null=True)

    class Meta:
        # Orders products so the newest listings appear first
        ordering = ['-created_at']
        verbose_name_plural = "Products"

    def __str__(self):
        # Returns the name of the product in the admin panel
        return self.name