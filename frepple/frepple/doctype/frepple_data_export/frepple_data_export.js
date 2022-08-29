// Copyright (c) 2022, Drayang Chua and contributors
// For license information, please see license.txt

frappe.ui.form.on('Frepple Data Export', {
	/*export_data_to_frepple(frm){
		var proceed = confirm("Are you sure you want to export the selected data to Frepple?");
		if (proceed) {
			frappe.msgprint(("Exporting Data To Frepple . . ."))
			frm.call({
				method:"export_data",
				args:{
					doc: frm.doc
				},
				callback:function(r){
					console.log(r.message)
				},
			})
		}
	},*/

	export_data_to_frepple(frm){
		var i = 0;
		var fields = frm.fields_dict;
		for (const field in fields)
			if(fields[field].df.fieldtype=="Check" && fields[field].value == 1) i = i+1;
		frappe.confirm(
			"("+i+") Fields are selected... Please confirm that you want to export them to Frepple",
			function(){
				frappe.msgprint(("Exporting Data To Frepple . . ."))
				frm.call({
					method:"export_data",
					args:{
						doc: frm.doc
					},
					callback:function(r){
						console.log(r.message)
					},
				})
			},
			function(){
				window.close();
			}
		)
	},
	
	select_all(frm){
		var fields = frm.fields_dict;
		for (const field in fields)
		{
			if(fields[field].df.fieldtype=="Check" && fields[field].df.read_only == 0)
			{
				frm.set_value(fields[field].df.fieldname,1);
			}
		}
	},
	deselect_all(frm){
		var fields = frm.fields_dict;
		for (const field in fields)
		{
			if(fields[field].df.fieldtype=="Check"  && fields[field].df.read_only == 0)
			{
				frm.set_value(fields[field].df.fieldname,0);
			}
		}
	}
});
