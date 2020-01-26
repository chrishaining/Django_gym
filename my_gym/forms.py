from django import forms

from .models import Member, Instructor, Session

class MemberForm(forms.ModelForm):
    # member = forms.ModelChoiceField(Member.objects.all())
    class Meta:
        model = Member
        fields = ('first_name', 'last_name')