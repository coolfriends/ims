from django.shortcuts import render
from .models import Sord, Invoice


def sales_invoice_order_report_static(request):

    template_name = "reports/sales_invoice_order_report_static.html"
    status_dict = {
        'C': 'Closed',
    }

    sord_queryset = Sord.objects.get(pk=2722)
    invoice_queryset = Invoice.objects.filter(in_sord_nu=2722)

    invoice_total = 0
    for invoice in invoice_queryset:
        invoice_total += invoice.in_tot_amt

    sord_balance = sord_queryset.so_tot_amt - invoice_total
    for invoice in invoice_queryset:
        if invoice.in_tot_amt == sord_queryset.so_tot_amt:
            sord_balance = 0

    return render(request, template_name, context={
        'sord': sord_queryset,
        'invoices': invoice_queryset,
        'status_dict': status_dict,
        'sord_balance': sord_balance,
    })
