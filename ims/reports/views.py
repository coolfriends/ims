from django.shortcuts import render
from .models import Sord, Invoice


def sales_invoice_order_report(request, pk):

    template_name = "reports/sales_invoice_order_report_static.html"
    sord_queryset = Sord.objects.get(so_sord_nu=pk)
    invoice_queryset = Invoice.objects.filter(in_sord_nu=pk).order_by("in_inv_dat")
    invoice_total_dict = {}

    invoice_total = 0
    for invoice in invoice_queryset:
        invoice_total += invoice.in_tot_amt
        if invoice.in_tot_amt == sord_queryset.so_tot_amt:
            invoice_total_dict[invoice.in_inv_num] = 0
        else:
            invoice_total_dict[invoice.in_inv_num] = sord_queryset.so_tot_amt - invoice_total

    sord_balance = sord_queryset.so_tot_amt - invoice_total
    for invoice in invoice_queryset:
        if invoice.in_tot_amt == sord_queryset.so_tot_amt:
            sord_balance = 0

    return render(request, template_name, context={
        'sord': sord_queryset,
        'invoices': invoice_queryset,
        'invoice_totals': invoice_total_dict,
        'sord_balance': sord_balance,
    })
