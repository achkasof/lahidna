from django.contrib import admin
from .models import Blogger, Musician, Personality, Artist, Scientist, Project, Description


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    exclude = ['id']


@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    exclude = ['id']


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    exclude = ['id']


@admin.register(Personality)
class PersonalityAdmin(admin.ModelAdmin):
    exclude = ['id']


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    exclude = ['id']


@admin.register(Scientist)
class ScientistAdmin(admin.ModelAdmin):
    exclude = ['id']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    exclude = ['id']
