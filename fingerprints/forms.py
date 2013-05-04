# encoding: utf-8
from django import forms
from models import FingerPrints, Human, ORIENT_TYPE, PATTERN_TYPE

class FingerPrintForm(forms.Form):
    pattern = forms.ChoiceField(choices=PATTERN_TYPE, label=u'тип',)
    orient = forms.ChoiceField(choices=ORIENT_TYPE, initial='N', label=u'ориентация', widget=forms.RadioSelect())
    rc_u = forms.IntegerField(required=False, label = u'уГС', widget=forms.TextInput(attrs={'style': 'width: 30px'}))
    rc_r = forms.IntegerField(required=False, label = u'рГС', widget=forms.TextInput(attrs={'style': 'width: 30px'}))
    
    
    #fio = forms.CharField(label = u'Ф.И.О', max_length=150, required = True, widget=forms.TextInput(attrs={'class':'inp1'}) )
    
    def save(self):
        pass
