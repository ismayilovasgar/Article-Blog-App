from django import forms


class RegisterFrom(forms.Form):
    username = forms.CharField(max_length=30, label="Username")
    password = forms.CharField(
        max_length=12, label="Password", widget=forms.PasswordInput
    )
    confirm = forms.CharField(
        max_length=12, label="Password Confirm", widget=forms.PasswordInput
    )

    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        confirm = self.cleaned_data["confirm"]

        if password and username and password != confirm:
            raise forms.ValidationError("Sifreler Uygunlasmir !!!")
