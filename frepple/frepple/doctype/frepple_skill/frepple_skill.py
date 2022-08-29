# -*- coding: utf-8 -*-
# Copyright (c) 2022, Drayang Chua and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe.model.document import Document

class FreppleSkill(Document):
	pass

@frappe.whitelist()
def fetch_skill_to_operation(source_name,target_doc=None):
	doc = json.loads(target_doc)
	# doc = frappe.get_doc("Frepple Resource", source_name)
	frappe.db.set_value('Frepple Operation Resource', source_name, {
		'skill': doc["name"],
	})
	return target_doc

@frappe.whitelist()
def fetch_skill_to_resource(source_name,target_doc=None):
	doc = json.loads(target_doc)
	new_resource_skill = frappe.new_doc("Frepple Resource Skill")
	new_resource_skill.resource = source_name
	new_resource_skill.skill = doc["name"]
	new_resource_skill.proficiency = 4
	new_resource_skill.insert()
	return target_doc