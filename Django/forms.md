# forms

## making manual forms
> 필요한 모든 정보가 나와있는 사이트: <br>
[how to render django form manually](https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html)

<br>

## to change a `forms.DateField` to use html date input instead of text input
  ```python
  class DateInput(forms.DateInput):
      input_type = 'date'

  class AForm(forms.Form):
    date = forms.DateField(widget=DateInput)
  ```