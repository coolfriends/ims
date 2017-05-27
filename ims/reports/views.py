from django.shortcuts import render
from .models import Sord, Invoice
from .forms import SalesInvoiceOrderReportForm


def sales_invoice_order_report_index(request):
    """
    Form view that takes Sales Order number and redirects to
    report template
    """
    template_name = "reports/sales_invoice_order_report_index.html"
    context = {}

    if request.method == 'POST':
        form = SalesInvoiceOrderReportForm(request.POST)

        if form.is_valid():
            pk = form.cleaned_data['sales_order_number']
            context = sales_invoice_order_report_context(pk)
    else:
        form = SalesInvoiceOrderReportForm

    context['form'] = form

    return render(request, template_name, context=context)


def sales_invoice_order_report_context(pk):
    """
    View for report that returns context dictionary
    """
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

    return {
        'sord': sord_queryset,
        'invoices': invoice_queryset,
        'invoice_totals': invoice_total_dict,
        'sord_balance': sord_balance,
    }


def sales_invoice_order_report_detail(request, pk):
    """
    Physical report view that takes DB objects from models.py,
    calculates invoice total and sales order balance,
    and renders into a Pure CSS styled HTML template
    """
    template_name = "reports/sales_invoice_order_report.html"
    sord_queryset = Sord.objects.get(so_sord_nu=pk)
    invoice_queryset = Invoice.objects.filter(in_sord_nu=pk).order_by("-in_inv_dat")
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
