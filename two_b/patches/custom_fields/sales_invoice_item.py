import frappe

def execute():
    custom_fields = {
        "Sales Invoice Item": [
            dict(
                fieldname="distributed_discount_amount",
                label="Distributed Discount Amount",
                fieldtype="Currency",
                insert_after="discount_amount",
                options="currency",
                no_copy=1,
                is_custom_field=1
            ),
            dict(
                fieldname="available_quantity_section",
                label="Available Quantity",
                fieldtype="Section Break",
                insert_after="section_break_eoec",
                is_custom_field=1
            ),
            dict(
                fieldname="column_break_ogff",
                fieldtype="Column Break",
                insert_after="actual_qty",
                is_custom_field=1
            ),
            dict(
                fieldname="company_total_stock",
                label="Qty (Company)",
                fieldtype="Float",
                insert_after="column_break_ogff",
                no_copy=1,
                read_only=1,
                is_custom_field=1
            ),
            dict(
                fieldname="pos_invoice",
                label="POS Invoice",
                fieldtype="Link",
                insert_after="delivered_qty",
                options="POS Invoice",
                no_copy=1,
                read_only=1,
                is_custom_field=1
            ),
            dict(
                fieldname="pos_invoice_item",
                label="POS Invoice Item",
                fieldtype="Data",
                insert_after="pos_invoice",
                no_copy=1,
                read_only=1,
                is_custom_field=1
            )
        ]
    }

    from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
    create_custom_fields(custom_fields)