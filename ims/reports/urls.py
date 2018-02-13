"""reports URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import sales_invoice_order_report_index
from .views import range_sales_invoice_order_report_index

urlpatterns = [
    url(r'^sales_invoice_order_report/$',
        sales_invoice_order_report_index,
        name='sales-invoice-order-report-index'
    ),

    url(r'^range_sales_invoice_order_report/$',
        range_sales_invoice_order_report_index,
        name='range-sales-invoice-order-report-index'
    ),
]
