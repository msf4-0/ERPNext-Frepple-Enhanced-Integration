// Copyright (c) 2022, Drayang Chua and contributors
// For license information, please see license.txt

frappe.ui.form.on('Frepple Settings', {
	test_delete:function(frm){
		frm.call({
			method:"test_delete",
			args:{
				doc: frm.doc
			},
			callback:function(r){
				console.log(r.message)
			},
		})
	}
	// refresh: function(frm) {
 
	// }
});
