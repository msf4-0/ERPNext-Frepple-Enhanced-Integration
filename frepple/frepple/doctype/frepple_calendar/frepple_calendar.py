# -*- coding: utf-8 -*-
# Copyright (c) 2022, Drayang Chua and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe.model.document import Document

class FreppleCalendar(Document):
	pass

@frappe.whitelist()
def fetch_available_2_location(source_name,target_doc=None):
	doc = json.loads(target_doc)
	# doc = frappe.get_doc("Frepple Resource", source_name)
	frappe.db.set_value('Frepple Location', source_name, {
		'available': doc["name"],
	})
	return target_doc

@frappe.whitelist()
def fetch_available_2_operation(source_name,target_doc=None):
	doc = json.loads(target_doc)
	# doc = frappe.get_doc("Frepple Operation", source_name)
	frappe.db.set_value('Frepple Operation', source_name, {
		'available_frepple_operation': doc["name"],
	})
	return target_doc

@frappe.whitelist()
def fetch_available_2_resource_available(source_name,target_doc=None):
	doc = json.loads(target_doc)
	# doc = frappe.get_doc("Frepple Resource", source_name)
	frappe.db.set_value('Frepple Resource', source_name, {
		'available': doc["name"],
	})
	return target_doc

@frappe.whitelist()
def fetch_available_2_resource_max_calendar(source_name,target_doc=None):
	doc = json.loads(target_doc)
	# doc = frappe.get_doc("Frepple Resource", source_name)
	frappe.db.set_value('Frepple Resource', source_name, {
		'maxcalendar_frepple': doc["name"],
	})
	return target_doc

@frappe.whitelist()
def fetch_available_2_supplier(source_name,target_doc=None):
	doc = json.loads(target_doc)
	# doc = frappe.get_doc("Frepple Resource", source_name)
	frappe.db.set_value('Frepple Supplier', source_name, {
		'available_supplier': doc["name"],
	})
	return target_doc

