from django import forms

class CardForm(forms.Form):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name:','aria-describedby':'Help'}))
    keyword = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Keyword:','id':'inputPassword{{ order.id }}'}))
    customize = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'5','id':'comment{{ order.id }}'}))
