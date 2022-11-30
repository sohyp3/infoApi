from django import forms 
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['browser_codeName','browser_language','cookies_enabled','platform','user_agent_header','timezone_utc','timezone_place','screen_size','battery_level']

