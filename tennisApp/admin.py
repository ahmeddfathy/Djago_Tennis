from django.contrib import admin

# Register your models here.
from .models import FirstSection , SecondSection , ThirdSection , FourthSection , SixSection , FifthSection , SixSection , Video


admin.site.register(FirstSection)
admin.site.register(SecondSection)

admin.site.register(ThirdSection)
admin.site.register(FourthSection)

admin.site.register(FifthSection)
admin.site.register(SixSection)

admin.site.register(Video)