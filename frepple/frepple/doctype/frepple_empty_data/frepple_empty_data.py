# -*- coding: utf-8 -*-
# Copyright (c) 2022, Drayang Chua and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, json
from frappe.model.document import Document
from frappe import _

class FreppleEmptyData(Document):
	pass

@frappe.whitelist()
def delete_data(doc):
	doc = json.loads(doc)

	deleted_data = []

	# Result
	if doc["frepple_manufacturing_order"]:
		delete_manufacturing_Order()
		deleted_data.append("Frepple Manufacturing Order")
		print("Frepple Manufacturing Order is deleted")
	if doc["frepple_purchase_order"]:
		delete_purchase_order()
		deleted_data.append("Frepple Purchase Order")
		print("Frepple Purchase Order is deleted")
	if doc["frepple_distribution_order"]:
		delete_distribution_order()
		deleted_data.append("Frepple Distribution Order")
		print("Frepple Distribution Order is deleted")

	# Demand
	if doc["frepple_demand"]:
		delete_sales_orders()
		deleted_data.append("Frepple Demand")
		print("Frepple Demand is deleted")
	
	# Manufacturing
	if doc["frepple_operation_resource"]:
		delete_operation_resources()
		deleted_data.append("Frepple Operation Resource")
		print("Frepple Operation Resource is deleted")
	if doc["frepple_operation_material"]:
		delete_operation_materials()
		deleted_data.append("Frepple Operation Materials")
		print("Frepple Operation Materials is deleted")
	if doc["frepple_operation"]:
		delete_operations()
		deleted_data.append("Frepple Operation")
		print("Frepple Operation is deleted")

	# Purchasing
	if doc["frepple_item_supplier"]:
		delete_item_suppliers()
		deleted_data.append("Frepple Item Supplier")
		print("Frepple Item Supplier is deleted")
	if doc["frepple_supplier"]:
		delete_suppliers()
		deleted_data.append("Frepple Supplier")
		print("Frepple Supplier is deleted")

	# Inventory
	if doc["frepple_buffer"]:
		delete_buffers()
		deleted_data.append("Frepple Buffer")
		print("Frepple Buffer is deleted")
	if doc["frepple_item_distribution"]:
		delete_item_distribution()
		deleted_data.append("Frepple Item Distribution")
		print("Frepple Item Distribution is deleted")

	# Capacity
	if doc["frepple_resource_skill"]:
		delete_resource_skills()
		deleted_data.append("Frepple Resource Skill")
		print("Frepple Resource Skill is deleted")
	if doc["frepple_resource"]:
		delete_resources()
		deleted_data.append("Frepple Resource")
		print("Frepple Resource is deleted")
	if doc["frepple_skill"]:
		delete_skills()
		deleted_data.append("Frepple Skill")
		print("Frepple Skill is deleted")

	# Sales
	if doc["frepple_item"]:
		delete_items()
		deleted_data.append("Frepple Item")
		print("Frepple Item is deleted")
	if doc["frepple_customer"]:
		delete_customers()
		deleted_data.append("Frepple Customer")
		print("Frepple Customer is deleted")
	if doc["frepple_location"]:
		delete_locations()
		deleted_data.append("Frepple Location")
		print("Frepple Location is deleted")

	#Additional data
	if doc["frepple_calendar_bucket"]:
		delete_calendar_buckets()
		deleted_data.append("Frepple Calendar Bucket")
		print("Frepple Calendar Bucket is deleted")
	if doc["frepple_calendar"]:
		delete_calendars()
		deleted_data.append("Frepple Calendar")
		print("Frepple Calendar is deleted")

	# Output msg 
	for data in deleted_data:
		frappe.msgprint(_("{0} Is Deleted").format(data))

def delete_sales_orders():
	items = frappe.db.sql(
		"""
		SELECT name
		FROM `tabFrepple Demand`
		"""
		,as_dict=1)

	for i in items:
		#print(i.name)
		item_doc= frappe.get_doc("Frepple Demand", i.name)
		#print(item_doc.name)
		frappe.delete_doc("Frepple Demand",item_doc.name, force=1,  for_reload=True)

def delete_operation_resources():
	items = frappe.db.sql(
		"""
		SELECT name
		FROM `tabFrepple Operation Resource`
		"""
		,as_dict=1)

	for i in items:
		#print(i.name)
		item_doc= frappe.get_doc("Frepple Operation Resource", i.name)
		#print(item_doc.name)
		frappe.delete_doc("Frepple Operation Resource",item_doc.name, force=1,  for_reload=True)

def delete_operation_materials():
	items = frappe.db.sql(
		"""
		SELECT name
		FROM `tabFrepple Operation Material`
		"""
		,as_dict=1)

	for i in items:
		#print(i.name)
		item_doc= frappe.get_doc("Frepple Operation Material", i.name)
		#print(item_doc.name)
		frappe.delete_doc("Frepple Operation Material",item_doc.name, force=1,  for_reload=True)

def delete_operations():
	items = frappe.db.sql(
		"""
		SELECT name
		FROM `tabFrepple Operation`
		"""
		,as_dict=1)

	for i in items:
		#print(i.name)
		item_doc= frappe.get_doc("Frepple Operation", i.name)
		#print(item_doc.name)
		frappe.delete_doc("Frepple Operation",item_doc.name, force=1, for_reload=True)

def delete_item_suppliers():
	items = frappe.db.sql(
		"""
		SELECT name
		FROM `tabFrepple Item Supplier`
		"""
		,as_dict=1)

	for i in items:
		#print(i.name)
		item_doc= frappe.get_doc("Frepple Item Supplier", i.name)
		#print(item_doc.name)
		frappe.delete_doc("Frepple Item Supplier",item_doc.name, force=1,  for_reload=True)

def delete_suppliers():
	items = frappe.db.sql(
		"""
		SELECT name
		FROM `tabFrepple Supplier`
		"""
		,as_dict=1)

	for i in items:
		#print(i.name)
		item_doc= frappe.get_doc("Frepple Supplier", i.name)
		#print(item_doc.name)
		frappe.delete_doc("Frepple Supplier",item_doc.name, force=1,  for_reload=True)

def delete_item_distribution():
	items = frappe.db.sql(
		"""
		SELECT name
		FROM `tabFrepple Item Distribution`
		"""
		,as_dict=1)

	for i in items:
		#print(i.name)
		item_doc= frappe.get_doc("Frepple Item Distribution", i.name)
		#print(item_doc.name)
		frappe.delete_doc("Frepple Item Distribution",item_doc.name, force=1,  for_reload=True)

def delete_buffers():
	items = frappe.db.sql(
		"""
		SELECT name
		FROM `tabFrepple Buffer`
		"""
		,as_dict=1)

	for i in items:
		#print(i.name)
		item_doc= frappe.get_doc("Frepple Buffer", i.name)
		#print(item_doc.name)
		frappe.delete_doc("Frepple Buffer",item_doc.name, force=1,  for_reload=True)

def delete_resource_skills():
	items = frappe.db.sql(
		"""
		SELECT name
		FROM `tabFrepple Resource Skill`
		"""
		,as_dict=1)

	for i in items:
		#print(i.name)
		item_doc= frappe.get_doc("Frepple Resource Skill", i.name)
		#print(item_doc.name)
		frappe.delete_doc("Frepple Resource Skill",item_doc.name, force=1,  for_reload=True)

def delete_skills():
	items = frappe.db.sql(
		"""
		SELECT name
		FROM `tabFrepple Skill`
		"""
		,as_dict=1)

	for i in items:
		#print(i.name)
		item_doc= frappe.get_doc("Frepple Skill", i.name)
		#print(item_doc.name)
		frappe.delete_doc("Frepple Skill",item_doc.name, force=1,  for_reload=True)

def delete_resources():
	items = frappe.db.sql(
		"""
		SELECT name
		FROM `tabFrepple Resource`
		"""
		,as_dict=1)

	for i in items:
		#print(i.name)
		item_doc= frappe.get_doc("Frepple Resource", i.name)
		#print(item_doc.name)
		frappe.delete_doc("Frepple Resource",item_doc.name, force=1,  for_reload=True)

def delete_locations():
	owner_list = frappe.db.sql(
		"""
		SELECT name, location_owner
		FROM `tabFrepple Location`
		ORDER BY location_owner
		"""
		,as_dict=1)

	delete_location_iteration_process(owner_list)

def delete_location_iteration_process(owner_list):
	
	#owner_nums = []
	#for i in owner_list:
	#	owner_nums.append(i.location_owner) if (i.location_owner not in owner_nums) & (i.location_owner != None) else owner_nums
	#print(owner_nums)

	for i in range(len(owner_list)):
		
		#print("\nPassing >> \n",owner_list)
		normal_list, owner_list = filter_locations(owner_list)
		
		for i in normal_list:
			item_doc= frappe.get_doc("Frepple Location", i.name)
			print("Deleting : ", item_doc.name)
			frappe.delete_doc("Frepple Location",item_doc.name, force=1,  for_reload=True)

		if len(owner_list) == 0:
			print("Aborted... No items to delete")
			break

def filter_locations(items):
	is_owner = 0
	normal_list = []
	owner_list = []
	for i in items:
		for j in items:
			if i.name == j.location_owner:
				is_owner = 1
				#print("Breaking")
				break
			elif i.name != j.location_owner:
				is_owner = 0

		if is_owner == 1:
			owner_list.append(i) if i.name not in owner_list else owner_list
			#print(i.name, " is owner")
		elif is_owner == 0:
			normal_list.append(i) if i.name not in normal_list else normal_list
			#print(i.name, " is not owner")

	# To ensure no owner has been added as location
	for location in normal_list:
		for owner in owner_list:
			if location.name == owner.name:
				#print(location.name, " was found as owner")
				normal_list.remove(location)

	#print("location items 2: ",normal_list)
	#print("owner items 2: ",owner_list)

	return normal_list, owner_list

'''def filter_locations(items):				# this will return list of normal and owner names only
	is_owner = 0
	normal_list = []
	owner_list = []
	for i in items:
		for j in items:
			if i.name == j.location_owner:
				is_owner = 1
				print("Breaking")
				break
			elif i.name != j.location_owner:
				is_owner = 0
		print("")
		if is_owner == 1:
			owner_list.append(i.name) if i.name not in owner_list else owner_list
			print(i.name, " is owner")
		elif is_owner == 0:
			normal_list.append(i.name) if i.name not in normal_list else normal_list
			print(i.name, " is not owner")

	print("location items 1: ",normal_list)
	print("owner items 1: ",owner_list)

	# To ensure no owner has been added as location
	for location in normal_list:
		for owner in owner_list:
			if location == owner:
				print(location, " was found as owner")
				normal_list.remove(location)

	print("location items 2: ",normal_list)
	print("owner items 2: ",owner_list)

	return normal_list, owner_list'''	
		
def delete_customers():
	items = frappe.db.sql(
		"""
		SELECT name
		FROM `tabFrepple Customer`
		"""
		,as_dict=1)

	for i in items:
		#print(i.name)
		item_doc= frappe.get_doc("Frepple Customer", i.name)
		#print(item_doc.name)
		frappe.delete_doc("Frepple Customer",item_doc.name, force=1,  for_reload=True)

def delete_items():
	items = frappe.db.sql(
		"""
		SELECT name, item_group, description
		FROM `tabFrepple Item`
		ORDER BY item_group
		"""
		,as_dict=1)
	
	delete_item_iteration_process(items)

def delete_item_iteration_process(owner_list):
	
	#owner_nums = []
	#for i in owner_list:
		#owner_nums.append(i.item_group) if (i.item_group not in owner_nums) & (i.item_group != None) else owner_nums
	#print(owner_nums)

	for i in range(len(owner_list)):
		
		#print("\nPassing >> \n",owner_list)
		normal_list, owner_list = filter_items(owner_list)

		for i in normal_list:
			item_doc= frappe.get_doc("Frepple Item", i.name)
			print("Deleting : ", item_doc.name)
			frappe.delete_doc("Frepple Item",item_doc.name, force=1,  for_reload=True)

		if len(owner_list) == 0:
			print("Aborted... No items to delete")
			break

def filter_items(items):
	is_owner = 0
	normal_list = []
	owner_list = []
	for i in items:
		for j in items:
			if i.name == j.item_group:
				is_owner = 1
				#print("Breaking")
				break
			elif i.name != j.item_group:
				is_owner = 0

		if is_owner == 1:
			owner_list.append(i) if i.name not in owner_list else owner_list
			#print(i.name, " is owner")
		elif is_owner == 0:
			normal_list.append(i) if i.name not in normal_list else normal_list
			#print(i.name, " is not owner")

	# To ensure no owner has been added as location
	for location in normal_list:
		for owner in owner_list:
			if location.name == owner.name:
				print(location.name, " was found as owner")
				normal_list.remove(location)

	#print("items 2: ",normal_list)
	#print("items owner 2: ",owner_list)

	return normal_list, owner_list

def delete_calendars():
	items = frappe.db.sql(
		"""
		SELECT name
		FROM `tabFrepple Calendar`
		"""
		,as_dict=1)

	for i in items:
		item_doc= frappe.get_doc("Frepple Calendar", i.name)
		frappe.delete_doc("Frepple Calendar",item_doc.name, force=1,  for_reload=True)

def delete_calendar_buckets():
	#test_delete_table()
	items = frappe.db.sql(
		"""
		SELECT name
		FROM `tabFrepple Calendar Bucket`
		"""
		,as_dict=1)

	for i in items:
		#print("deleting: ",i.name)
		calendar_list = delete_calendars_table(i.name)
		item_doc= frappe.get_doc("Frepple Calendar Bucket", i.name)
		#print(item_doc.name)
		frappe.delete_doc("Frepple Calendar Bucket",item_doc.name, force=1,  for_reload=True)

def delete_calendars_table(bucket):		#delete table row "bucket (name)" inside a doctype
	items = frappe.db.sql(
		"""
		SELECT name
		FROM `tabFrepple Calendar`
		"""
		,as_dict=1)
	calendar_list=[]
	for i in items:
		delete_table = []
		item_doc= frappe.get_doc("Frepple Calendar", i.name)
		for d in item_doc.get("calendar_bucket"):
			if d.calendar_bucket == bucket:
				delete_table.append(d) if d not in delete_table else delete_table
				calendar_list.append(i.name) if i.name not in calendar_list else calendar_list

		for d in delete_table:
			item_doc.remove(d) 
			#print(d.calendar_bucket," is deleted from ", i.name)
		
		item_doc.save()
		frappe.db.commit()
		#print("the table is deleted")
	return calendar_list

'''def test_delete_table():		#this test row deleting in Frepple Manufacturing Order
	items = frappe.db.sql(
		"""
		SELECT name
		FROM `tabFrepple Manufacturing Order`
		"""
		,as_dict=1)
	delete_table =[]
	for i in items:
		item_doc= frappe.get_doc("Frepple Manufacturing Order", i.name)
		for d in item_doc.get("resource"):
			item_doc.remove(d) 
		item_doc.save()
		frappe.db.commit()
			#delete_table.append(d) if d not in delete_table else delete_table
			#print(d.resource," is added to list")
		#for d in delete_table:
			#item_doc.remove(d) 
			#print(("the raw {0} is deleted").format(d))'''

def delete_manufacturing_Order():
	items = frappe.db.sql(
		"""
		SELECT name
		FROM `tabFrepple Manufacturing Order`
		"""
		,as_dict=1)

	for i in items:
		#print(i.name)
		item_doc= frappe.get_doc("Frepple Manufacturing Order", i.name)
		#print(item_doc.name)
		frappe.delete_doc("Frepple Manufacturing Order",item_doc.name, force=1,  for_reload=True)	

def delete_purchase_order():
	items = frappe.db.sql(
		"""
		SELECT name
		FROM `tabFrepple Purchase Order`
		"""
		,as_dict=1)

	for i in items:
		#print(i.name)
		item_doc= frappe.get_doc("Frepple Purchase Order", i.name)
		#print(item_doc.name)
		frappe.delete_doc("Frepple Purchase Order",item_doc.name, force=1,  for_reload=True)

def delete_distribution_order():
	items = frappe.db.sql(
		"""
		SELECT name
		FROM `tabFrepple Distribution Order`
		"""
		,as_dict=1)

	for i in items:
		#print(i.name)
		item_doc= frappe.get_doc("Frepple Distribution Order", i.name)
		#print(item_doc.name)
		frappe.delete_doc("Frepple Distribution Order",item_doc.name, force=1,  for_reload=True)
