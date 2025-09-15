import frappe

def execute():
    custom_fields = {
        "Sales Order": [
            dict(
                fieldname="has_unit_price_items",
                label="Has Unit Price Items",
                fieldtype="Check",
                insert_after="skip_delivery_note",
                default="0",
                no_copy=1,
                allow_on_submit=1,
                is_custom_field=1
            ),
            dict(
                fieldname="last_scanned_warehouse",
                label="Last Scanned Warehouse",
                fieldtype="Data",
                insert_after="scan_barcode",
                is_virtual=1,
                depends_on="eval: doc.last_scanned_warehouse",
				allow_on_submit=1,
                is_custom_field=1
            )
        ]
    }

    from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
    create_custom_fields(custom_fields)
