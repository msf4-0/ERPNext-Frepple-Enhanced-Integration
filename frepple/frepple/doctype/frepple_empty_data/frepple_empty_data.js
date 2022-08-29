
frappe.ui.form.on('Frepple Empty Data', {
	/*delete_data(frm){
		var i = 0;
		var fields = frm.fields_dict;
		for (const field in fields)
			if(fields[field].df.fieldtype=="Check" && fields[field].value == 1) i = i+1;
		var proceed = confirm("("+i+") Fields are selected . . . \nPlease confirm that you want to delete them permanently?");
		if (proceed) {
			frappe.msgprint(("Deleting Data . . ."))
			frm.call({
				method:"delete_data",
				args:{
					doc: frm.doc
				},
				callback:function(r){
					console.log(r.message)
				},
			})
		}
	},*/

	delete_data(frm){
		var i = 0;
		var fields = frm.fields_dict;
		for (const field in fields)
			if(fields[field].df.fieldtype=="Check" && fields[field].value == 1) i = i+1;
		frappe.confirm(
			"("+i+") Fields are selected... Please confirm that you want to delete them permanently",
			function(){
				frappe.msgprint(("Deleting Data . . ."))
				frm.call({
					method:"delete_data",
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

	frepple_calendar(frm){
		if (frm.doc.frepple_calendar == 1){
			frm.set_value("frepple_calendar_bucket", 1);
		}
		else {
			frm.set_value("frepple_calendar_bucket", 0);
		}
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
				//frm.set_value("frepple_calendar",0);
				//frm.set_value("frepple_calendar_bucket",0);
			}
		}
	}
});
