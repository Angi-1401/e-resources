from django.contrib import admin

from apps.forum.models import Forum, Post, Reply, Comment


class ForumAdmin(admin.ModelAdmin):
    list_display = ("resource",)


class PostAdmin(admin.ModelAdmin):
    list_display = ("forum", "user", "timestamp")


class ReplyAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "timestamp")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("reply", "user", "timestamp")


admin.site.register(Forum, ForumAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Reply, ReplyAdmin)
admin.site.register(Comment, CommentAdmin)
