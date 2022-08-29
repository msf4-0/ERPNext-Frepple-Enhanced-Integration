# -*- coding: utf-8 -*-
# Copyright (c) 2022, Drayang Chua and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe.model.document import Document

class FreppleSupplier(Document):
	pass 

@frappe.whitelist()
def fetch_item_to_supplier(source_name,target_doc=None):
	doc = json.loads(target_doc)
	new_item_suppier = frappe.new_doc("Frepple Item Supplier")
	new_item_suppier.item = source_name
	new_item_suppier.supplier = doc["name"]
	new_item_suppier.time = "00:00:00"
	new_item_suppier.time1 = "00:00:00"
	new_item_suppier.insert()
	return target_doc