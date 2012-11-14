from models import FoodOption, Vote
from django.contrib import admin

class FoodOptionAdmin(admin.ModelAdmin):
    pass
    
class VoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(FoodOption, FoodOptionAdmin)
admin.site.register(Vote, VoteAdmin)