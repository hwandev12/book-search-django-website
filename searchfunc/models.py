from django.db import models

# create book card class
class BookCardsModel(models.Model):
    class Meta:
        verbose_name = 'Card Books'
        verbose_name_plural = 'Card Books'
    
    book_cover = models.ImageField()
    book_name = models.CharField(max_length=100)
    book_subtitle = models.CharField(max_length=100)
    book_description = models.TextField(max_length=300)
    full_description = models.TextField(max_length=700)
    # shop details
    shop_details_description = models.TextField(max_length=700, blank=True)
    shop_cost = models.IntegerField(default=1, blank=True)
    # category model with foreignkey
    category = models.ForeignKey('BookCategoryModel', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return str(self.book_name)
    
# book category model
class BookCategoryModel(models.Model):
    class Meta:
        verbose_name = 'Book Category'
        verbose_name_plural = 'Book Category'
        
    name = models.CharField(max_length=90, null=True, blank=True)
    
    def __str__(self):
        return self.name