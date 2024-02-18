from django.contrib import admin
from .models import Jogadores, Times

# Register your models here.
#mdel = Jogadores
admin.site.register(Jogadores)

#model = Times
admin.site.register(Times)
