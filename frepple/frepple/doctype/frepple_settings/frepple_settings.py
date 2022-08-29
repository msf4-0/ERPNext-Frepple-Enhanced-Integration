# -*- coding: utf-8 -*-
# Copyright (c) 2022, Drayang Chua and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe,json
from frappe.model.document import Document
from frappe import _

from datetime import datetime
from datetime import time
from datetime import timedelta
from frappe.utils import add_to_date

class FreppleSettings(Document):
	pass

@frappe.whitelist()
def test_delete(doc):
	DocName = "Frepple Purchase Order"
	rskill = frappe.db.sql(
		"""
		SELECT name
		FROM `tabDocName`
		"""
		,as_dict=1)

	for i in rskill:
		#print(i.name)
		item_doc= frappe.get_doc(DocName, i.name)
		print(item_doc.name)
		delete = frappe.delete_doc(DocName,item_doc.name)
    
	#return delete

