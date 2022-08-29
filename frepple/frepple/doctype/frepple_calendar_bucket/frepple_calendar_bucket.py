# -*- coding: utf-8 -*-
# Copyright (c) 2022, Drayang Chua and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, json
from frappe.model.document import Document
from frappe import _
from frepple.frepple.doctype.frepple_empty_data.frepple_empty_data import delete_calendars_table
 
class FreppleCalendarBucket(Document):

	@frappe.whitelist()
	def add_to_calendar(self):
		exist = 0
		if(self.calendar):
			doc= frappe.get_doc("Frepple Calendar",self.calendar)

			
			calendar_buckets = frappe.db.sql(
				"""
				SELECT fc.name, fccb.calendar_bucket 
				FROM `tabFrepple Calendar` fc, `tabFrepple Calendar Calendar Bucket` fccb
				WHERE fc.name = fccb.parent
				""",
			as_dict=1)
			# condition check to prevent adding duplicate row 
			for calendar_bucket in calendar_buckets:
				print(calendar_bucket)
				if calendar_bucket.calendar_bucket == self.name:
					exist = 1


			if exist != 1: #if the calendar bucket is not added to the calendar before
				row = doc.append("calendar_bucket",{})
				row.calendar_bucket = self.name
				row.start_datetime=self.start_datetime
				row.end_datetime = self.end_datetime
				row.start_time = self.start_time
				row.end_time = self.end_time
				row.monday = self.monday
				row.tuesday = self.tuesday
				row.wednesday = self.wednesday
				row.thursday = self.thursday
				row.friday = self.friday
				row.saturday = self.saturday
				row.sunday = self.sunday

				frappe.msgprint(_("{0} calendar is updated.").format(self.calendar))

				row.save(ignore_permissions=True, ignore_version=True)

				row.reload()

	@frappe.whitelist()
	def check_priority(self):
		duplicate = 0

		if(self.calendar):
			doc= frappe.get_doc("Frepple Calendar",self.calendar)
	
			
			calendar_buckets = frappe.db.sql(
				"""
				SELECT name, priority,calendar
				FROM `tabFrepple Calendar Bucket`
				WHERE calendar = %s
				""",
			doc.name,as_dict=1)

			for calendar_bucket in calendar_buckets:
				print(calendar_bucket)
				if self.priority == calendar_bucket.priority:
					duplicate = 1

		return duplicate

	pass

@frappe.whitelist()
def remove_calendar_bucket(doc):
	doc = json.loads(doc)
	
	calendar_list = delete_calendars_table(doc["name"])
	if calendar_list:
		for calendar in calendar_list:
			print("calendar : ", calendar)
			print(("{0} is removed from {1}").format(doc["name"], calendar))
			frappe.msgprint(("{0} is removed from {1}").format(doc["name"], calendar))
	else:
		print("Nothing")
		frappe.msgprint(("{0} is not linked to any calendar").format(doc["name"]))
		print(("{0} is not linked to any calendar").format(doc["name"]))

@frappe.whitelist()
def fetch_bucket_to_calendar(source_name,target_doc=None):
	# doc is a list of all the fields of the bucket
	# source_name is the selected destination doctype
	exist = 0
	bucket = json.loads(target_doc)
	doc= frappe.get_doc("Frepple Calendar",source_name)
	current_row = doc.get("calendar_bucket")

	# condition check to prevent adding duplicate row 
	for d in current_row:
		if d.calendar_bucket == bucket["name"]:
			exist = 1
			print("Bucket already exist")
			frappe.msgprint(("{0} already exist in {1}").format(bucket["name"], source_name))

	if exist != 1: #if the calendar bucket is not added to the calendar before
		row = doc.append("calendar_bucket",{})
		row.calendar_bucket = bucket["name"]
		row.start_datetime=["start_datetime"]
		row.end_datetime = bucket["end_datetime"]
		row.start_time = bucket["start_time"]
		row.end_time = bucket["end_time"]
		row.monday = bucket["monday"]
		row.tuesday = bucket["tuesday"]
		row.wednesday = bucket["wednesday"]
		row.thursday = bucket["thursday"]
		row.friday = bucket["friday"]
		row.saturday = bucket["saturday"]
		row.sunday = bucket["sunday"]

		row.save(ignore_permissions=True, ignore_version=True)
		row.reload()	
		frappe.msgprint(("{0} is successfully added to {1}").format(bucket["name"], source_name))

	return target_doc 
