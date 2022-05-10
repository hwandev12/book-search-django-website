from django.contrib import admin
from .models import *

# import book models
admin.site.register(BookCardsModel)
admin.site.register(BookCategoryModel)
# import slider models
admin.site.register(SliderImagesContent)
# import Who we are models
admin.site.register(WhoWeAreModel)
# import essential page here
admin.site.register(EssentialsPageModel)
# import essential right content
admin.site.register(EssentialRightContent)
# import Count page model
admin.site.register(CountPageModel)
# import books to read page model
admin.site.register(BooksToRead)
