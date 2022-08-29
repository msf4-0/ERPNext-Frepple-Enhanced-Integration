// Copyright (c) 2022, Drayang Chua and contributors
// For license information, please see license.txt

frappe.ui.form.on('Frepple Supplier', {
	refresh: function(frm) {
		frm.add_custom_button(__('Sellect item to be supplied'), function() {
			erpnext.utils.map_current_doc({
				method: "frepple.frepple.doctype.frepple_supplier.frepple_supplier.fetch_item_to_supplier",
				source_doctype: "Frepple Item",
				target: frm,
				date_field: "creation",
				setters: {
				},
				get_query_filters: {
					// docstatus: 1
				}
			})
		}, //__("Assign resource to")
		);
	}
});
