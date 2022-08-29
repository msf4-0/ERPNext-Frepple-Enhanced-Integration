// Copyright (c) 2022, Drayang Chua and contributors
// For license information, please see license.txt

frappe.ui.form.on('Frepple Operation', {
	setup: function(frm) {
		frm.set_query('operation_owner', function() {
			return {
				filters: [
					['Frepple Operation', 'type', '=', 'routing'],
					// ['Work Order', 'qty', '>','`tabWork Order`.produced_qty'],
					// ['Work Order', 'company', '=', frm.doc.company]
				]
			}
		});
	},

	validate: function(frm) {
		if(frm.doc.type == 'fixed_time' || frm.doc.type == 'time_per' || frm.doc.type == 'alternate' || frm.doc.type == 'split'){
			frm.set_value('operation_temp', frm.doc.operation);
			frm.refresh_field('operation_temp');
		}
		if(frm.doc.type == 'routing'){
			frm.set_value('operation_temp', frm.doc.operation_routing);
			frm.refresh_field('operation_temp');
		}
	},

	type:function(frm){
		if (frm.doc.type !== "time_per"){
			frm.set_value('duration_per_unit', "00:00:00");
			frm.refresh_field('duration_per_unit');
		}
	}
})

