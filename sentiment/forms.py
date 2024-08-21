from django import forms
from dataclasses import dataclass
from sentiment.sentiment import get_sentiment


@dataclass
class Sentiment:
    tag: str
    msg: str


sentiments = {
    0: ("danger", "Statement `{}` is Negative"),
    1: ("success", "Statement `{}` is Positive"),
    2: ("secondary", "Statement `{}` is Neutral"),
}


class SentimentForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SentimentForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    prompt = forms.CharField(
        min_length=3,
        max_length=1000,
        required=True,
        label=False,
        widget=forms.TextInput(attrs={"autofocus": True}),
    )

    def get_sentiment(self) -> Sentiment:
        prediction = get_sentiment(self.cleaned_data["prompt"])
        tag, msg = sentiments.get(prediction, 2)
        statement = Sentiment(tag, msg.format(self.cleaned_data["prompt"][0:50]))
        return statement

    def save(self) -> Sentiment:
        return self.get_sentiment()
