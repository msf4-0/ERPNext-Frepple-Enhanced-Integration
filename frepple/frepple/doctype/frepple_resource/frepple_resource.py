# -*- coding: utf-8 -*-
# Copyright (c) 2022, Drayang Chua and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe.model.document import Document

class FreppleResource(Document):
	pass

@frappe.whitelist()
def fetch_resource_to_skill(source_name,target_doc=None):
	doc = json.loads(target_doc)
	new_resource_skill = frappe.new_doc("Frepple Resource Skill")
	new_resource_skill.resource = doc["name"]
	new_resource_skill.skill = source_name
	new_resource_skill.proficiency = 4
	new_resource_skill.insert()
	return target_doc

@frappe.whitelist()
def fetch_resource_to_operation(source_name,target_doc=None):
	doc = json.loads(target_doc)
	# doc is a list of all the fields of the resource
	# source_name is the selected destination doctype
	new_op_resource = frappe.new_doc("Frepple Operation Resource")
	new_op_resource.resource = doc["name"]
	if doc["employee_check"]:
		new_op_resource.employee_check = 1 
	new_op_resource.operation = source_name
	new_op_resource.proficiency = 4
	new_op_resource.insert()
	return target_doc 

@frappe.whitelist()
def fetch_resource_to_item_supplier(source_name,target_doc=None):
	doc = json.loads(target_doc)
	frappe.db.set_value('Frepple Item Supplier', source_name, {
		'resource': doc["name"],
	})
	return target_doc

@frappe.whitelist()
def fetch_resource_to_item_distribution(source_name,target_doc=None):
	doc = json.loads(target_doc)
	frappe.db.set_value('Frepple Item Distribution', source_name, {
		'resource': doc["name"],
	})
	return target_doc