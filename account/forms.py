from django import forms


def field_style():
    styles_string = " "

    # List of what you want to add to style the field
    styles_list = [
        "height: 30px ;",
        "margin:15px 0px ;",
        "border-radius:5px ;",
        "font-size:18px;",
    ]

    # Converting the list to a string
    styles_string = styles_string.join(styles_list)
    # or
    # styles_string = ' '.join(styles_list)

    return styles_string


class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        label="Username",
        widget=forms.TextInput(attrs={"class": "myfieldclass", "style": field_style()}),
    )
    password = forms.CharField(
        max_length=12,
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "myfieldclass", "style": field_style()}
        ),
    )
    confirm = forms.CharField(
        max_length=12,
        label="Password Confirm",
        widget=forms.PasswordInput(
            attrs={"class": "myfieldclass", "style": field_style()}
        ),
    )

    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        confirm = self.cleaned_data["confirm"]

        if password and username and password != confirm:
            raise forms.ValidationError("Sifreler Uygunlasmir !!!")

        values = {
            "username": username,
            "password": password,
        }

        return values


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        label="Username",
        widget=forms.TextInput(attrs={"class": "myfieldclass", "style": field_style()}),
    )
    password = forms.CharField(
        max_length=12,
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "myfieldclass", "style": field_style()}
        ),
    )
