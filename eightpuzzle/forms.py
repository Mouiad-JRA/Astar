from django import forms


class AstarForm(forms.Form):
    input_state = forms.Textarea()
    end_state = forms.Textarea()


