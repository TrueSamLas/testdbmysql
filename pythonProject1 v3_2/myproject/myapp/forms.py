from django import forms
from .models import Products, Register, Percent


class ModuleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModuleForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Products
        fields = ['title', 'descriprions']
        labels = {
            'title': 'Название',
            'descriprions': 'Описание',
        }


class PurchaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PurchaseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Register
        fields = ['product', 'quantite', 'price']
        labels = {
            'product': 'Товар',
            'quantite': 'Количество',
            'price': 'Цена',
        }


class SellForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SellForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Register
        fields = ['product', 'quantite']
        labels = {
            'product': 'Товар',
            'quantite': 'Количество',
        }


class PercentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PercentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Percent
        fields = ['rate']
        labels = {
            'rate': 'Рейт',
        }