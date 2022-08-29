// Copyright (c) 2022, Drayang Chua and contributors
// For license information, please see license.txt

var clicked = false;
frappe.ui.form.on('Frepple Calendar', {
	refresh: function(frm) {
		frm.add_custom_button(__('Add Calendar to :'), function() {
			if (!clicked){
				clicked = true;
				frm.add_custom_button(__('Frepple Location'), function() {
					erpnext.utils.map_current_doc({
						method: "frepple.frepple.doctype.frepple_calendar.frepple_calendar.fetch_available_2_location",
						source_doctype: "Frepple Location",
						target: frm,
						date_field: "creation",
						setters: {
						},
						get_query_filters: {
							// docstatus: 1
						}
					})
				}, __("Available field for"));
	
				frm.add_custom_button(__('Frepple Operation'), function() {
					erpnext.utils.map_current_doc({
						method: "frepple.frepple.doctype.frepple_calendar.frepple_calendar.fetch_available_2_operation",
						source_doctype: "Frepple Operation",
						target: frm,
						date_field: "creation",
						setters: {
						},
						get_query_filters: {
							// docstatus: 1
						}
					})
				}, __("Available field for"));
	
				frm.add_custom_button(__('Frepple Resource'), function() {
					erpnext.utils.map_current_doc({
						method: "frepple.frepple.doctype.frepple_calendar.frepple_calendar.fetch_available_2_resource_available",
						source_doctype: "Frepple Resource",
						target: frm,
						date_field: "creation",
						setters: {
						},
						get_query_filters: {
							// docstatus: 1
						}
					})
				}, __("Available field for"));
	
				frm.add_custom_button(__('Frepple Supplier'), function() {
					erpnext.utils.map_current_doc({
						method: "frepple.frepple.doctype.frepple_calendar.frepple_calendar.fetch_available_2_supplier",
						source_doctype: "Frepple Supplier",
						target: frm,
						date_field: "creation",
						setters: {
						},
						get_query_filters: {
							// docstatus: 1
						}
					})
				}, __("Available field for"));
	
				frm.add_custom_button(__('Frepple Resource'), function() {
					erpnext.utils.map_current_doc({
						method: "frepple.frepple.doctype.frepple_calendar.frepple_calendar.fetch_available_2_resource_max_calendar",
						source_doctype: "Frepple Resource",
						target: frm,
						date_field: "creation",
						setters: {
						},
						get_query_filters: {
							// docstatus: 1
						}
					})
				}, __("Maximum Calendar field for"));
				}
			}
		)
	}
});

