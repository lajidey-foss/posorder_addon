# - 
# Copyright 2021 Jide Olayinka
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe import _
from frappe.utils.data import add_days, date_diff, today
from frappe.utils import flt
from frappe.model.mapper import get_mapped_doc

from erpnext.controllers.accounts_controller import add_taxes_from_tax_template

GLOBAL_AUTO_ORDER_SERIES = 'SM-SO-.YYYY.-'


@frappe.whitelist()
def make_sales_order(doc, method):
    if not frappe.db.get_single_value('Order Addon Setting', 'auto_sop_posting'):
        return
    #print(f'\n\n\n\n Pick from Hooks \n\n\n\n')
    if doc.is_return or doc.return_against:
        return

    '''
    doc.posa_pos_opening_shift
        and doc.pos_profile
        and doc.is_pos
        and doc.posa_delivery_date
        and not doc.update_stock
        and frappe.get_value("POS Profile", doc.pos_profile, "posa_allow_sales_order")
    '''

    if (
        doc.pos_profile
        and doc.is_pos
    ):
        sales_order_doc = create_sales_order(doc)

def create_sales_order(source_name, target_doc=None, ignore_permissions=True):
    #print(f'\n\n\n\n firstline create: \n\n\n\n')
    sales_order = frappe.get_doc({
        "doctype": "Sales Order",
        "customer": source_name.customer,
        "company": source_name.company,
        "currency": source_name.currency,
        "conversion_rate": source_name.conversion_rate,
        "selling_price_list": source_name.selling_price_list,
        "price_list_currency": source_name.price_list_currency,
        "set_warehouse": source_name.set_warehouse,
        "total_qty": source_name.total_qty,
        "base_total": source_name.base_total,
        "base_net_total": source_name.base_net_total,
        "total": source_name.total,
        "net_total": source_name.net_total,
        "base_grand_total": source_name.base_grand_total,
        "source": source_name.source,
        "naming_series" : GLOBAL_AUTO_ORDER_SERIES,
        "doc.ignore_pricing_rule" : 1,
        "posting_date": source_name.posting_date,
        "delivery_date": source_name.posting_date
    })
    #SO Item
    for item in source_name.items:
        sales_order.append("items", {
            "item_code": item.item_code,
            "customer_item_code": item.customer_item_code,
            "item_name": item.item_name,
            "qty": item.qty,
            "stock_uom": item.stock_uom,
            "uom": item.uom,
            "conversion_factor":item.conversion_factor,
            "rate": item.rate,
            "amount": item.amount,
            "stock_uom_rate" : item.stock_uom_rate,
            "warehouse": item.warehouse,
            "target_warehouse": item.target_warehouse,
            "actual_qty": item.actual_qty
        })
    
    #sales_order.insert()    
    sales_order.flags.ignore_permissions = True
    frappe.flags.ignore_account_permission = True
    sales_order.ignore_pricing_rule = 1
    sales_order.set_missing_values()

    sales_order.save()
    sales_order.submit()
    #frappe.msgprint("Sales order created.")

    #print(f'\n\n\n\n in closing: {sales_order.name} \n\n\n\n')
    return sales_order.name

@frappe.whitelist()
def update_invoice(data):
    data = json.loads(data)
    if data.get("name"):
        invoice_doc = frappe.get_doc("Sales Invoice", data.get("name"))
        invoice_doc.update(data)
    else:
        invoice_doc = frappe.get_doc(data)

    invoice_doc.set_missing_values()
    invoice_doc.flags.ignore_permissions = True
    frappe.flags.ignore_account_permission = True

    for item in invoice_doc.items:
        add_taxes_from_tax_template(item, invoice_doc)

    if frappe.get_cached_value(
        "POS Profile", invoice_doc.pos_profile, "posa_tax_inclusive"
    ):
        if invoice_doc.get("taxes"):
            for tax in invoice_doc.taxes:
                tax.included_in_print_rate = 1

    invoice_doc.save()
    return invoice_doc