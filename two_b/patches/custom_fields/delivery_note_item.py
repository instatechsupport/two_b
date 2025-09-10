import frappe

def execute():
    custom_fields = {
        "Delivery Note Item": [
            dict(
                fieldname="distributed_discount_amount",
                label="Distributed Discount Amount",
                fieldtype="Currency",
                insert_after="discount_amount",
                options="currency",
                is_custom_field=1
            ),
            dict(
                fieldname="company_total_stock",
                label="Qty (Company)",
                fieldtype="Float",
                insert_after="column_break_atna",
                no_copy=1,
                read_only=1,
                columns="150px",
                is_custom_field=1
            ),
            dict(
                fieldname="against_pick_list",
                label="Against Pick List",
                fieldtype="Link",
                insert_after="against_sales_invoice_item",
                options="Pick List",
                no_copy=1,
                is_custom_field=1
            ),
        ]
    }

    from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
    create_custom_fields(custom_fields)