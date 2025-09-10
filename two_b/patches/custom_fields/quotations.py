import frappe

def execute():
    custom_fields = {
        "Quotation": [
            dict(
                fieldname="has_unit_price_items",
                label="Has Unit Price Items",
                fieldtype="Check",
                insert_after="company_email",
                default="0",
                no_copy=1,
                hidden=1
            ),
            dict(
                fieldname="last_scanned_warehouse",
                label="Last Scanned Warehouse",
                fieldtype="Data",
                insert_after="scan_barcode",
                is_virtual=1,
                depends_on="eval: doc.last_scanned_warehouse"
            ),

            dict(
                fieldname="disable_rounded_total",
                label="Disable Rounded Total",
                fieldtype="Check",
                insert_after="rounded_total",
                default="1"
            ),
            dict(
                fieldname="company_contact_person",
                label="Company Contact Person",
                fieldtype="Link",
                insert_after="column_break_87",
                options="Contact"
            )
        ]
    }

    from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
    create_custom_fields(custom_fields)