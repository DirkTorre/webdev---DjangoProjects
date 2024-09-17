from django.contrib import admin

from .models import Movie, Actor, Role

# admin.site.register(Movie)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ("last_name", "first_name")
# admin.site.register(Actor)
# admin.site.register(Role)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','year', 'imdb_id')

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_year', 'imdb_id')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('movie_id', 'actor_id', 'role')