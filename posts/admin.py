from django.contrib import admin

from .models import Post


#custom admin options/functions --> check out documentation
class PostAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "created_at", "updated_at"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post



#built-in function that registers model to site!
admin.site.register(Post, PostAdmin)
