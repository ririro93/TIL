# form_validation
> [django docs](https://docs.djangoproject.com/en/3.1/ref/forms/validation/)

happens when is_valid() is called on a form

## process
1. to_python()
    - error if value is not correct datatype
2. validate()
    - field-specific validation that coerces correct datatype
3. run_validators()
    - runs all field validators -> no need to override
4. Field.clean()
    - runs 1~3 + returns clean data -> stored in cleaned_data
5. **`Form.clean_<fieldname>()`**
    - returned value replaces cleaned_data already cleaned by `clean()` method
    - Always return a value to use as the new cleaned data, even if this method didn't change it.
6. **`Form.clean()`**
    - validation that requires access to multiple form fields