from django.db import models
from django.contrib.auth.models import User    
from django.db import models  
from tastypie.models import create_api_key 
from django.db.models.signals import post_delete, post_save, pre_save

models.signals.post_save.connect(create_api_key, sender=User)

class FoodOption(models.Model):
    name = models.CharField(max_length=30)
    votes = models.IntegerField()
    
    class Meta:
        ordering = ['-votes']
    
    def __unicode__(self):
        return self.name

class Vote(models.Model):
    food_option = models.ForeignKey(FoodOption)
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.food_option.name

def add_vote(sender, **kwargs):
    obj = kwargs['instance']
    obj.food_option.votes = Vote.objects.filter(food_option=obj.food_option).count()
    obj.food_option.save()
    
def remove_vote(sender, **kwargs):
    obj = kwargs['instance']
    if hasattr(obj, 'food_option'):
        obj.food_option.votes -=1
        obj.food_option.save()

def check_vote_unique(sender, **kwargs):
    obj = kwargs['instance']
    Vote.objects.filter(user=obj.user).delete()

pre_save.connect(check_vote_unique, sender=Vote)
post_save.connect(add_vote, sender=Vote)
post_delete.connect(remove_vote, sender=Vote)