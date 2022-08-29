// Copyright (c) 2022, Drayang Chua and contributors
// For license information, please see license.txt


frappe.ui.form.on('Frepple Skill', {
	refresh: function(frm) {
		frm.add_custom_button(__('Frepple Operation Resource'), function() {
			erpnext.utils.map_current_doc({
				method: "frepple.frepple.doctype.frepple_skill.frepple_skill.fetch_skill_to_operation",
				source_doctype: "Frepple Operation Resource",
				target: frm,
				date_field: "creation",
				setters: {
				},
				get_query_filters: {
					// docstatus: 1
				}
			})
		}, __("Assign skill to"));
	}
});

frappe.ui.form.on('Frepple Skill', {
	refresh: function(frm) {
		frm.add_custom_button(__('Frepple Resource Skill'), function() {
			erpnext.utils.map_current_doc({
				method: "frepple.frepple.doctype.frepple_skill.frepple_skill.fetch_skill_to_resource",
				source_doctype: "Frepple Resource",
				target: frm,
				date_field: "creation",
				setters: {
				},
				get_query_filters: {
					// docstatus: 1
				}
			})
		}, __("Assign skill to"));
	}
});