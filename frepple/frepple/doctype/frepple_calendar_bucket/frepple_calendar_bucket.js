// Copyright (c) 2022, Drayang Chua and contributors
// For license information, please see license.txt

frappe.ui.form.on('Frepple Calendar Bucket', {
	after_save:function(frm){
		frm.call({
			method:"add_to_calendar",
			doc: frm.doc,
			// method:"make_request",
			callback:function(r){
			}
		});
	},

	validate:function(frm){
		frm.call({
			method:"check_priority",
			doc: frm.doc,
			// method:"make_request",
			callback:function(r){
				var duplicate = r.message
				if (duplicate){
					frappe.validated = false
					frappe.msgprint({
						title: __('Notice'),
						indicator: 'red',
						message: __('Priority is duplicate. Please modify it.')
					});
				}
			}
		});
	}
});

frappe.ui.form.on('Frepple Calendar Bucket', {
	refresh: function(frm) {
		frm.add_custom_button(__('Remove this bucket from all Frepple Calendars'), function() {
			var proceed = confirm("Are you sure you want to Remove this bucket from all Frepple Calendars?");
			if (proceed) {
				frm.call({
					method:"remove_calendar_bucket",
					args:{
						doc: frm.doc
					},
					callback:function(r){
						console.log(r.message)
					},
				})
			}
		});
	}
});

frappe.ui.form.on('Frepple Calendar Bucket', {
	refresh: function(frm) {
		frm.add_custom_button(__('Add this bucket to Frepple Calendar'), function() {
			erpnext.utils.map_current_doc({
				method: "frepple.frepple.doctype.frepple_calendar_bucket.frepple_calendar_bucket.fetch_bucket_to_calendar",
				source_doctype: "Frepple Calendar",
				target: frm,
				date_field: "creation",
				setters: {
				},
				get_query_filters: {
					// docstatus: 1
				}
			})
		});
	}
});

frappe.ui.form.on('Frepple Calendar Bucket', {
	refresh: function(frm) {
		
	}
});