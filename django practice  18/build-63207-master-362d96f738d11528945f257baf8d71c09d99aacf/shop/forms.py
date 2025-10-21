from django import forms


class PersonalInformation(forms.Form):
    GENDERS = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    gender = forms.ChoiceField(choices=GENDERS)
    full_name = forms.CharField(max_length=60 , min_length=5)
    height = forms.IntegerField(min_value= 70 , max_value= 250)
    age = forms.IntegerField(min_value= 14 , max_value= 99)


    def clean_full_name(self) :

        name = self.cleaned_data.get('full_name')

        if name.istitle() :

            return name

        else :

            raise forms.ValidationError("Error") 
    

