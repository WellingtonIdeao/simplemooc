from django import forms


class ContactCourse(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(lanel='E-mail')
    message = forms.CharField(
        label='Messagem/Dúvida',
        widget=forms.Textarea
    )
