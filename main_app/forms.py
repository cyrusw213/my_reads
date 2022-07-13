from django.forms import ModelForm
from .models import LastRead

class LastReadForm(ModelForm):
  class Meta:
    model = LastRead
    fields = ['date', 'num_stars']