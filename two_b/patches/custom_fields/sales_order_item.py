import frappe

def execute():
    custom_fields = {
        "Sales Order Item": [
            dict(
                fieldname="distributed_discount_amount",
                label="Distributed Discount Amount",
                fieldtype="Currency",
                insert_after="discount_amount",
                options="currency",
                is_custom_field=1
            ),
            dict(
                fieldname="amount_currency",
                label="Amount Currency",
                fieldtype="Currency",
                insert_after="rate_ui",
                reqd=1,
                in_list_view=1,
                options="currency",
                is_custom_field=1
            ),
            dict(
                fieldname="exchange_rate",
                label="Exchange Rate",
                fieldtype="Float",
                insert_after="col_break3",
                default="1",
                precision=4,
                is_custom_field=1
            ),
            dict(
                fieldname="available_quantity_section",
                label="Available Quantity",
                fieldtype="Section Break",
                insert_after="column_break_69",
                is_custom_field=1
            ),
            dict(
                fieldname="column_break_jpky",
                fieldtype="Column Break",
                insert_after="actual_qty",
                is_custom_field=1
            ),
            dict(
                fieldname="company_total_stock",
                label="Qty (Company)",
                fieldtype="Float",
                insert_after="column_break_jpky",
                no_copy=1,
                read_only=1,
                is_custom_field=1
            ),
            dict(
                fieldname="accounting_dimensions_section",
                label="Accounting Dimensions",
                fieldtype="Section Break",
                insert_after="column_break_ihdh",
                read_only=1,
                is_custom_field=1
            ),
            dict(
                fieldname="cost_center",
                label="Cost Center",
                fieldtype="Link",
                insert_after="accounting_dimensions_section",
                options="Cost Center",
                default=":Company",
                columns="120px",
                is_custom_field=1
            ),
            dict(
                fieldname="column_break_ihdh",
                fieldtype="Column Break",
                insert_after="cost_center",
                is_custom_field=1
            ),
            dict(
                fieldname="project",
                label="Project",
                fieldtype="Link",
                insert_after="column_break_ihdh",
                options="Project",
                is_custom_field=1
            )
        ]
    }

    from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
    create_custom_fields(custom_fields)