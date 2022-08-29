// Copyright (c) 2022, Drayang Chua and contributors
// For license information, please see license.txt

frappe.ui.form.on('Frepple Integration Data Fetching', {

	/*get_data_for_frepple(frm){
		//frappe.msgprint(("Fetching Data To Frepple Custom App..."))
		var proceed = confirm("Are you sure you want to fetch the selected data from ERPNext?");
		if (proceed) {
			frm.call({
				method:"fetch_data",
				args:{
					doc: frm.doc
				},
				callback:function(r){
					console.log(r.message)
				},
			})
		}
	},*/
	
	get_data_for_frepple(frm){
		var i = 0;
		var fields = frm.fields_dict;
		for (const field in fields)
			if(fields[field].df.fieldtype=="Check" && fields[field].value==1 && fields[field].df.read_only==0) i = i+1;
		frappe.confirm(
			"("+i+") Fields are selected... Please confirm to begin the fetching process",
			function(){
				frm.call({
					method:"fetch_data",
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
