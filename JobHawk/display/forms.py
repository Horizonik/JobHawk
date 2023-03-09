from django import forms


class SearchForm(forms.ModelForm):
    keywords = forms.CharField(label='Search', max_length=100, required=False)

    widgets = {
        'keywords': forms.TextInput(attrs={'class': 'search-input'}),
    }

    def clean_keywords(self):
        keywords = self.cleaned_data['keywords']

        if keywords:
            return keywords.split()
        return []
