from django import forms

from calculus.models import Answer

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            "answer_1",
            "answer_2",
            "answer_3",
            "answer_4",
            "answer_5",
            "answer_6",
            "answer_7",
            "answer_8",
            "answer_9",
            "answer_10",
        ]
