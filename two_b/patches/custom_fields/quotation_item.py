import frappe

def execute():
    custom_fields = {
        "Quotation Item": [
            dict(
                fieldname="description_ar",
                label="Description AR",
                fieldtype="Text Editor",
                insert_after="description",
                translatable=1,
                is_custom_field=1
            ),
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
            dict(
                fieldname="currency_new",
                label="Currency",
                fieldtype="Select",
                insert_after="section_break1",
                options="EGP\nUSD",
                no_copy=1,
                read_only=1,
                is_system_generated=1,
                is_custom_field=1
            ),
            dict(
                fieldname="test",
                label="Material Cost",
                fieldtype="Float",
                insert_after="currency_new",
                read_only=1,
                is_system_generated=1,
                is_custom_field=1
            ),
            dict(
                fieldname="material_cost_dummy",
                label="Material Cost Dummy",
                fieldtype="Float",
                insert_after="test",
                read_only=1,
                is_custom_field=1
            ),
            dict(
                fieldname="transportation",
                label="Transportation",
                fieldtype="Currency",
                insert_after="material_cost_dummy",
                read_only=1,
                is_system_generated=1,
                is_custom_field=1
            ),
            dict(
                fieldname="column_break_34",
                fieldtype="Column Break",
                insert_after="transportation",
                is_custom_field=1
            ),
            dict(
                fieldname="exchange_rate",
                label="Exchange Rate",
                fieldtype="Float",
                insert_after="column_break_34",
                reqd=1,
                precision=2,
                no_copy=1,
                is_system_generated=1,
                is_custom_field=1
            ),
            dict(
                fieldname="section_break_47",
                fieldtype="Section Break",
                insert_after="exchange_rate",
                is_system_generated=1,
                is_custom_field=1
            ),
            dict(
                fieldname="egp_amount",
                label="EGP Amount",
                fieldtype="Currency",
                insert_after="section_break_47",
                options="Company:company:default_currency",
                depends_on="eval:doc.test_currency_2=='EGP'",
                read_only=1,
                hidden=1,
                is_system_generated=1,
                is_custom_field=1
            ),
            dict(
                fieldname="item_type",
                label="Item Type",
                fieldtype="Select",
                insert_after="egp_amount",
                options="Main\nAlt",
                no_copy=1,
                is_system_generated=1,
                is_custom_field=1
            ),
            dict(
                fieldname="foreign_amount",
                label="Foreign Amount",
                fieldtype="Currency",
                insert_after="item_type",
                depends_on="eval:doc.test_currency_2=='USD'",
                read_only=1,
                hidden=1,
                is_system_generated=1,
                is_custom_field=1
            ),
            dict(
                fieldname="delivery_location",
                label="Delivery Location",
                fieldtype="Select",
                insert_after="additional_notes",
                options="\nCompany Stores\nClient\nxWork",
                is_custom_field=1
            )
        ]
    }

    from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
    create_custom_fields(custom_fields)