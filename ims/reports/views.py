from django.shortcuts import render
from .models import Sord, Invoice, Inventor
from .forms import SalesInvoiceOrderReportForm
from .forms import RangeSalesInvoiceOrderReportForm


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


def range_sales_invoice_order_report_index(request):
    """
    Form view that takes multiple Sales Order numbers and redirects to
    multi-report template
    """
    template_name = "reports/range_sales_invoice_order_report_index.html"
    context = {}

    if request.method == 'POST':
        form = RangeSalesInvoiceOrderReportForm(request.POST)

        if form.is_valid():
            start = form.cleaned_data['begin_sales_order_number']
            end = form.cleaned_data['end_sales_order_number']
            context = range_sales_invoice_order_report_context(start, end)

    else:
        form = RangeSalesInvoiceOrderReportForm

    context['form'] = form

    return render(request, template_name, context=context)


def make_buy_report_index(request):
    """
    Form view that takes Sales Order number and redirects to
    report template
    """
    template_name = "reports/make_buy_report_index.html"
    context = make_buy_report_context()

    return render(request, template_name, context=context)


def sales_invoice_order_report_context(pk):
    """
    View for report that returns context dictionary
    """
    sord_queryset = None
    invoice_queryset = None
    sord_balance = None
    invoice_total_dict = {}

    try:
        sord_queryset = Sord.objects.get(so_sord_nu=pk)
        invoice_queryset = Invoice.objects.filter(in_sord_nu=pk).order_by("in_inv_dat")
        invoice_total_dict = {}

        invoice_total = 0
        sord_balance = 0

        for invoice in invoice_queryset:
            invoice_total += invoice.in_tot_amt
            if invoice.in_tot_amt == sord_queryset.so_tot_amt:
                invoice_total_dict[invoice.in_inv_num] = 0
            elif invoice.in_tot_amt > sord_queryset.so_tot_amt:
                invoice_total_dict[invoice.in_inv_num] = sord_queryset.so_tot_amt - invoice.in_tot_amt
            else:
                invoice_total_dict[invoice.in_inv_num] = sord_queryset.so_tot_amt - invoice_total

            sord_balance = sord_queryset.so_tot_amt - invoice_total
            for invoice in invoice_queryset:
                if invoice.in_tot_amt == sord_queryset.so_tot_amt:
                    sord_balance = 0

    except Sord.DoesNotExist:
        sord_queryset = "bad_query"

    return {
        'sord': sord_queryset,
        'invoices': invoice_queryset,
        'invoice_totals': invoice_total_dict,
        'sord_balance': sord_balance,
    }


def range_sales_invoice_order_report_context(start, end):
    context_list = []

    for pk in range(start, end+1):
        context = sales_invoice_order_report_context(pk)
        context_list.append(context)

    return {
        'sords': context_list,
    }


def make_buy_report_context():
    inventor_queryset = Inventor.objects.all()

    return {
        'inventors': inventor_queryset,
    }
