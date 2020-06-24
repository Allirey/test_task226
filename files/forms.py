from django import forms
import datetime as dt


class FileForm(forms.Form):
    file = forms.FileField()
    expire = forms.ChoiceField(choices=(
        (dt.timedelta(minutes=1).total_seconds(), '1 minute'),
        (dt.timedelta(minutes=5).total_seconds(), '5 minutes'),
        (dt.timedelta(hours=1).total_seconds(), '1 hour'),
        (dt.timedelta(days=1).total_seconds(), '1 day'),
        (dt.timedelta(days=7).total_seconds(), '7 days'),))
