from django import forms

from .models import Member, Instructor, Session

class MemberForm(forms.ModelForm):
    # member = forms.ModelChoiceField(Member.objects.all())
    class Meta:
        model = Member
        fields = ('first_name', 'last_name')

class SessionForm(forms.ModelForm):
    # session = forms.ModelChoiceField(Session.objects.all())
    class Meta:
        model = Session
        fields = ('title', 'instructor')

class InstructorForm(forms.ModelForm):
    # instructor = forms.ModelChoiceField(Instructor.objects.all())
    class Meta:
        model = Instructor
        fields = ('first_name', 'last_name')