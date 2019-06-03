from django import forms


class InsertingDataForm(forms.Form):
    product_id = forms.IntegerField(
        label='Enter Your Product id',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'product id',
                'class': 'form-control'
            }
        )
    )
    product_name = forms.CharField(
        label='Enter Your Product name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'product name',
                'class': 'form-control'
            }
        )
    )
    product_cost = forms.IntegerField(
        label='Enter Your Product Cost',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'product cost',
                'class': 'form-control'
            }
        )
    )
    product_color = forms.CharField(
        label='Enter Your Product Color',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'product color',
                'class': 'form-control'
            }
        )
    )
    product_class = forms.CharField(
        label='Enter Your Product Class',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'product class',
                'class': 'form-control'
            }
        )
    )
    customer_name = forms.CharField(
        label='Enter Your Customer Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'customer name',
                'class': 'form-control'
            }
        )
    )
    customer_mobile = forms.IntegerField(
        label='Enter Your Customer Mobile',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'customer mobile',
                'class': 'form-control'
            }
        )
    )
    customer_email = forms.EmailField(
        label='Enter Your Customer Email',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'customer email',
                'class': 'form-control'
            }
        )
    )

class UpdatingDataForm(forms.Form):
    product_id = forms.IntegerField(
        label='Enter Your Product id',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'product id',
                'class': 'form-control'
            }
        )
    )
    product_cost = forms.IntegerField(
        label='Enter Your product cost',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'product cost',
                'class': 'form-control'
            }
        )
    )

class DeletingDataForm(forms.Form):
    product_id = forms.IntegerField(
        label='Enter Your Product id',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'product id',
                'class': 'form-control'
            }
        )
    )
