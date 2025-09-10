import frappe

def execute():
    custom_fields = {
        "Quotation Item": [
            dict(
                fieldname="available_quantity_section",
                label="Available Quantity",
                fieldtype="Section Break",
                insert_after="description_ar",
                is_custom_field=1
            ),
            dict(
                fieldname="column_break_ylrv",
                fieldtype="Column Break",
                insert_after="actual_qty",
                is_custom_field=1
            ),
            dict(
                fieldname="company_total_stock",
                label="Qty (Company)",
                fieldtype="Float",
                insert_after="column_break_ylrv",
                non_negative=1,
                no_copy=1,
                read_only=1,
                hidden=1,
                is_custom_field=1
            ),
        ]
    }

    from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
    create_custom_fields(custom_fields)