from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Seu nome', max_length=100)
    email = forms.EmailField(label='Seu e-mail')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)
