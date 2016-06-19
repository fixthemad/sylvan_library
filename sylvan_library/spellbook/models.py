from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.regex_helper import Choice

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    
class Subtype(models.Model):
    name = models.CharField(max_length = 50, unique = True)

class Block(models.Model):
    name = models.CharField(max_length = 200, unique = True)
    release_date = models.DateField()

class Set(models.Model):
    code = models.CharField(max_length = 10, unique = True)
    release_date = models.DateField(blank = True, null = True)
    name = models.CharField(max_length = 200, unique = True)
    
    block = models.ForeignKey('Block', null = True)
    
class Rarity(models.Model):
    symbol = models.CharField(max_length = 1, unique = True)
    name = models.CharField(max_length = 15, unique = True)
    display_order = models.IntegerField(unique = True)

class Card(models.Model):
    cost = models.CharField(max_length = 50, blank = True, null = True)
    cmc = models.IntegerField()
    colour = models.IntegerField()
    colour_identity = models.IntegerField()
    colour_count = models.IntegerField()
    type = models.CharField(max_length = 100, blank = True, null = True)
    subtype = models.CharField(max_length = 100, blank = True, null = True)
    power = models.CharField(max_length = 20, blank = True, null = True)
    num_power = models.FloatField()
    toughness = models.CharField(max_length = 20, blank = True, null = True)
    num_toughness = models.FloatField()
    loyalty = models.CharField(max_length = 20, blank = True, null = True)
    num_loyalty = models.FloatField()
    rules_text = models.CharField(max_length = 1000, blank = True, null = True)
    
class CardPrinting(models.Model):
    flavour_text = models.CharField(max_length = 350, blank = True, null = True)
    artist = models.CharField(max_length = 100)
    collector_number = models.IntegerField(blank = True, null = True)
    collector_letter = models.CharField(max_length = 1, blank = True, null = True)
    original_text = models.CharField(max_length = 1000, blank = True, null = True)
    original_type = models.CharField(max_length = 200, blank = True, null = True)
    
    set = models.ForeignKey('Set')
    card = models.ForeignKey('Card')
    rarity = models.ForeignKey('Rarity')
    
class CardPrintingLanguage(models.Model):
    
    language = models.CharField(max_length = 50)
    card_name = models.CharField(max_length = 200)
    
    card_printing = models.ForeignKey('CardPrinting')
    
class UserOwnedCard(models.Model):
    
    count = models.IntegerField()
    
    card_printing_language = models.ForeignKey('CardPrintingLanguage')
    owner = models.ForeignKey(User)
    
class UserCardChange(models.Model):
    
    difference = models.IntegerField()
    
    card_printing_language = models.ForeignKey('CardPrintingLanguage')
    owner = models.ForeignKey(User)
    
class CardLink(models.Model):
    
    card_from = models.ForeignKey('Card', related_name = 'cardFrom')
    card_to = models.ForeignKey('Card', related_name = 'cardTo')
    
    type = models.CharField(max_length = 1)
    
class CardRuling(models.Model):
    
    date = models.DateField()
    text = models.CharField(max_length = 1000)
    
    card = models.ForeignKey('Card')
    
class CardTag(models.Model):
    
    name = models.CharField(max_length = 200)
    
class CardTagLink(models.Model):
    
    tag = models.ForeignKey('CardTag')
    card = models.ForeignKey('Card')
    
class Deck(models.Model):
    
    date_created = models.DateField()
    last_modiifed = models.DateField()
    
    name = models.CharField(max_length = 200)
    owner = models.ForeignKey(User)
    
class DeckCard(models.Model):
    
    count = models.IntegerField()
    
    card = models.ForeignKey('Card')
    deck = models.ForeignKey('Deck')
    