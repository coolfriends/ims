from django import forms


class SalesInvoiceOrderReportForm(forms.Form):
    """
    Form class to pass sales order number as PK to report
    """
    sales_order_number = forms.IntegerField(label='',
                                            widget=forms.TextInput(attrs={'placeholder': 'Sales Order Number'}))
