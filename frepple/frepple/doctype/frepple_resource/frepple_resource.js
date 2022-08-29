// Copyright (c) 2022, Drayang Chua and contributors
// For license information, please see license.txt
 
frappe.ui.form.on('Frepple Resource', {
	// refresh: function(frm) {
	validate: function(frm) {
		if(frm.doc.workstation_check){
			frm.set_value('name1', frm.doc.workstation);
			frm.refresh_field('name1');
		}
		if(frm.doc.employee_check){
			frm.set_value('name1', frm.doc.employee);
			frm.refresh_field('name1');
		}
	}
	//employee_check:function(frm){
	//	if (frm.doc.employee_check){
	//		frm.set_value('resource_owner','Operator')
	//	}
	//},

	//workstation_check:function(frm){
	//	if (frm.doc.workstation_check){
	//		frm.set_value('resource_owner','Workstation')
	//	}
	//}
	
	// }
});

frappe.ui.form.on('Frepple Resource', {
	refresh: function(frm) {
		frm.add_custom_button(__('Frepple Resource Skill'), function() {
			erpnext.utils.map_current_doc({
				method: "frepple.frepple.doctype.frepple_resource.frepple_resource.fetch_resource_to_skill",
				source_doctype: "Frepple Skill",
				target: frm,
				date_field: "creation",
				setters: {
				},
				get_query_filters: {
					// docstatus: 1
				}
			})
		}, __("Assign resource to"));
	}
});

frappe.ui.form.on('Frepple Resource', {
	refresh: function(frm) {
		frm.add_custom_button(__('Frepple Operation Resource'), function() {
			erpnext.utils.map_current_doc({
				method: "frepple.frepple.doctype.frepple_resource.frepple_resource.fetch_resource_to_operation",
				source_doctype: "Frepple Operation",
				target: frm,
				date_field: "creation",
				setters: {
				},
				get_query_filters: {
					// docstatus: 1
				}
			})
		}, __("Assign resource to"));
	}
});

frappe.ui.form.on('Frepple Resource', {
	refresh: function(frm) {
		frm.add_custom_button(__('Frepple Item Supplier'), function() {
			erpnext.utils.map_current_doc({
				method: "frepple.frepple.doctype.frepple_resource.frepple_resource.fetch_resource_to_item_supplier",
				source_doctype: "Frepple Item Supplier",
				target: frm,
				date_field: "creation",
				setters: {
				},
				get_query_filters: {
					// docstatus: 1
				}
			})
		}, __("Assign resource to"));
	}
});

frappe.ui.form.on('Frepple Resource', {
	refresh: function(frm) {
		frm.add_custom_button(__('Frepple Item Distribution'), function() {
			erpnext.utils.map_current_doc({
				method: "frepple.frepple.doctype.frepple_resource.frepple_resource.fetch_resource_to_item_distribution",
				source_doctype: "Frepple Item Distribution",
				target: frm,
				date_field: "creation",
				setters: {
				},
				get_query_filters: {
					// docstatus: 1
				}
			})
		}, __("Assign resource to"));
	}
});