from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    #forma 03 de usar widget
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs = {'class': 'classe-a classe-b',
    #                  'placeholder': 'Aqui veio do __init__'
    #      }
    #     ),
    #     label = 'Primeiro nome',
    #     help_text='Texto de ajuda usuario'
    # )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

        #forma 02 de usar widget
        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Aqui veio do __init__'

        # })
    picture = forms.ImageField(
               widget=forms.FileInput(
                      attrs={
                             'accept' : 'image/*',
                      }
               )
        )
    class Meta:
        model = models.Contact
        fields = ('first_name','last_name','phone','email','description', 'category','picture')

        #forma 01 de usar widget
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs = {
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui'
        #         }
        #     )
        # }

    def clean(self):
        cleaned_data = self.cleaned_data()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )
            self.add_error('first_name', msg)
            self.add_error('last_name',msg)
            
        return super().clean()
       
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Mensagem de erro do clean_first_name',
                    code= 'invalid'
                )
            )
        return first_name
        