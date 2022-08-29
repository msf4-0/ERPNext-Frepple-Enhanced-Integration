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

from frappe.integrations.utils import make_get_request, make_post_request, create_request_log
from frappe.utils import get_request_session

import requests
from requests.structures import CaseInsensitiveDict

from frepple.frepple.doctype.frepple_data_export.frepple_data_export import get_frepple_params,export_sales_orders

class FreppleRunPlan(Document):
	pass

@frappe.whitelist()
def run_plan(doc):
	doc = json.loads(doc)

	if doc["update_frepple"]:
		export_sales_orders()
		export_manufacturing_orders()
		export_purchase_orders()

	constraint= 0
	plantype = 1
	# filter = "/execute/api/runplan/?"
	
	if doc['constraint']:
		plantype = 1
	if doc['unconstraint']:
		plantype = 2
	if doc['capacity']:
		constraint = constraint + 4
	if doc['lead_time']:
		constraint = constraint + 1
	if doc['release_fence']:
		constraint = constraint + 8

	filter = "/execute/api/runplan/?constraint="+ str(constraint)+"&plantype="+ str(plantype)+"&env=supply"
	frepple_settings = frappe.get_doc("Frepple Settings")
	temp_url = frepple_settings.url.split("//")
	url = "http://"+ frepple_settings.username + ":" + frepple_settings.password + "@" + temp_url[1] + filter
	print(url + "-----------------------------------------------------------------------")
	headers= {
		'Content-type': 'application/json; charset=UTF-8',
		'Authorization': frepple_settings.authorization_header,
	}

	output = make_post_request(url,headers=headers, data=None)

	frappe.msgprint(
		msg='Plan have been runned successfully.',
		title='Success',
	)

	return output

@frappe.whitelist()
def generate_result(doc):
	doc = json.loads(doc)

	import_datas = []

	# Import manufacturing order
	if doc["manufacturing_orders"]:
		data = import_manufacturing_order()
		import_datas.append("Manufacturing Order Result")
		generate_manufacturing_order(data)
		print("Manufacturing order result was successfuly imported")

	# Import purchase order
	if doc["purchase_orders"]:
		data = import_purchase_order()
		import_datas.append("Purchase Order Result")
		generate_purchase_order(data)
		print("Purchase order result was successfuly imported")

	# Import distribution order
	if doc["distribution_orders"]:
		data = import_distribution_order()
		import_datas.append("Distribution Order Result")
		generate_distribution_order(data)
		print("Distribution order result was successfuly imported")

	# Output msg 
	for import_data in import_datas:
		frappe.msgprint(_("{0} is imported.").format(import_data))


def export_manufacturing_orders():
	api = "manufacturingorder" #equivalent work order
	url,headers = get_frepple_params(api=api,filter=None)
	
	mos = frappe.db.sql(
		"""
		SELECT latest_reference,operation,status,quantity
		FROM `tabFrepple Manufacturing Order`
		""",
	as_dict=1)
		
	for mo in mos:
		#print(mo)
		data = json.dumps({
			"reference": mo.latest_reference,
			# "operation": mo.operation,
			"status": mo.status,
			# "quantity": mo.quantity,
		})
		output = make_post_request(url,headers=headers, data=data)

def export_purchase_orders():
	api = "purchaseorder" #equivalent purchase order
	url,headers = get_frepple_params(api=api,filter=None)
	
	pos = frappe.db.sql(
		"""
		SELECT latest_reference,supplier,status
		FROM `tabFrepple Purchase Order`
		""",
	as_dict=1)
		
	for po in pos:
		#print(po)
		data = json.dumps({
			"reference": po.latest_reference,
			# "supplier": po.supplier,
			"status": po.status,
		})
		output = make_post_request(url,headers=headers, data=data)



def import_manufacturing_order():
	api = "manufacturingorder"
	
	''' With filtering'''
	# filter = "?name=SAL-ORDER-0002"
	# filter = None
	# filter = "?status__contain=open"
	# url,headers = get_frepple_params(api=None,filter=filter)
	
	#filter = "?status=proposed&operation_in=BOM"
	# filter = "?operation_in=BOM"
	
	url,headers = get_frepple_params(api=api,filter=None)
	outputs = make_get_request(url,headers=headers)
	# print(type(outputs))
	# idx = 0
	# for output in outputs:
	# 	print(output["operation"])
	# 	print(output["operation"].split("@"))
	# 	if (len(output["operation"].split("@")) > 1): #routing type operation should only have 1 element, use this to filter out the routing type
	# 		print("Delete")
	# 		del outputs[idx]
	# 	idx = idx + 1

	# Delete dictionary from list using list comprehension
	res = [output for output in outputs if not (len(output["operation"].split("@")) > 1)]
	return res

def generate_manufacturing_order(data):

	for i in data:
		#print(i["plan"])
		# idx = 0
		# demand = (list(i["plan"]["pegging"].keys())[idx])
		demands = list(i["plan"]["pegging"].keys())
		resource_list = list(i["resources"])
		material_list = list(i["materials"])

		if not frappe.db.exists("Frepple Manufacturing Order", i["reference"]):
			new_doc = frappe.new_doc("Frepple Manufacturing Order")
			new_doc.reference = i["reference"]
			new_doc.latest_reference = i["reference"]
			new_doc.operation = i["operation"]
			new_doc.status = i["status"]
			new_doc.quantity = i["quantity"]
			new_doc.completed_quantity = i["quantity_completed"]
			new_doc.start_date = datetime.fromisoformat(i["startdate"])
			new_doc.end_date = datetime.fromisoformat(i["enddate"])
			new_doc.demand = demands[0]
			for resource in resource_list:
				new_doc.append('resource', {
					'reference': i["reference"],
					'resource': resource["resource"],
					'resource_quantity': resource["quantity"]
				})
			for material in material_list:
				new_doc.append('material', {
					'reference': i["reference"],
					'material': material["item"],
					'material_quantity': material["quantity"]
				})
			new_doc.insert()

		elif frappe.db.exists("Frepple Manufacturing Order", i["reference"]):
				frappe.db.set_value('Frepple Manufacturing Order', i["reference"], {
					#'latest_reference': i["reference"],
					'operation': i["operation"],
					'status': i["status"],
					'demand' : demands[0],
					'quantity': i["quantity"],
					#'completed_quantity': i["quantity_completed"],
					'start_date': datetime.fromisoformat(i["startdate"]),
					'end_date': datetime.fromisoformat(i["enddate"])
 				}) 
 
	''' Draft
		#To load data into table
		doc = frappe.get_doc("Frepple Manufacturing Order", i["reference"])
		for resource in resource_list:
			doc.append('resource', {
				'reference': i["reference"],
				'resource': resource["resource"],
				'resource_quantity': resource["quantity"]
			})
		for material in material_list:
			doc.append('material', {
				'reference': i["reference"],
				'material': material["item"],
				'material_quantity': material["quantity"]
			})
		doc.save()


		demands = (list(i["plan"]["pegging"].keys()))
		for demand in demands:
			mos = frappe.db.sql(
				"""
				SELECT name,demand
				FROM `tabFrepple Manufacturing Order`
				WHERE demand = %s
				""",
			demand,as_dict=1)
			#print(mos)
			# if not frappe.db.exists("Frepple Manufacturing Order",i["reference"]):
			if not frappe.db.exists("Frepple Manufacturing Order",i["reference"]) and len(mos)== 0:
				#create new document
				new_doc = frappe.new_doc("Frepple Manufacturing Order")
				new_doc.reference = i["reference"]
				new_doc.latest_reference = i["reference"]
				new_doc.operation = i["operation"]
				new_doc.status = i["status"]
				new_doc.quantity = i["quantity"]
				new_doc.completed_quantity = i["quantity_completed"]
				new_doc.start_date = datetime.fromisoformat(i["startdate"])
				new_doc.end_date = datetime.fromisoformat(i["enddate"])
				new_doc.demand = demand
				new_doc.insert()
				#print(new_doc.name)
			elif frappe.db.exists("Frepple Manufacturing Order",i["reference"]) and len(mos)== 0:
				continue
			else:#update
				if frappe.db.exists("Frepple Manufacturing Order",mos[0].name):
					existing_doc = frappe.get_doc("Frepple Manufacturing Order",mos[0].name)
					#print(existing_doc)
					frappe.db.set_value('Frepple Manufacturing Order', mos[0].name, #Update the status
					{
						'latest_reference': i["reference"],
						'operation': i["operation"],
						'status': i["status"],
						'quantity': i["quantity"],
						# 'completed_quantity': i["quantity_completed"],
						'start_date': datetime.fromisoformat(i["startdate"]),
						'end_date': datetime.fromisoformat(i["enddate"])
					})
	'''
					# existing_doc.reference = i["reference"]
					# existing_doc.operation = i["operation"]
					# existing_doc.status = i["status"]
					# existing_doc.quantity = i["quantity"]
					# existing_doc.completed_quantity = i["quantity_completed"]
					# existing_doc.start_date = datetime.fromisoformat(i["startdate"])
					# existing_doc.end_date = datetime.fromisoformat(i["enddate"])
					# existing_doc.save(ignore_permissions=True, ignore_version=True)
					# existing_doc.reload()


def import_purchase_order():
	api = "purchaseorder"
	
	''' With filtering'''
	# filter = "?name=SAL-ORDER-0002"
	# filter = None
	# filter = "?status__contain=open"
	# url,headers = get_frepple_params(api=None,filter=filter)
	#filter = "?status=proposed"
	
	url,headers = get_frepple_params(api=api,filter=None)
	output = make_get_request(url,headers=headers)

	return output

def generate_purchase_order(data):
	for i in data:
		#print(i)
		demands = list(i["plan"]["pegging"].keys())

		if not frappe.db.exists("Frepple Purchase Order",i["reference"]):
			new_doc = frappe.new_doc("Frepple Purchase Order")
			new_doc.reference = i["reference"]
			new_doc.latest_reference = i["reference"]
			new_doc.supplier = i["supplier"]
			new_doc.status = i["status"]
			new_doc.ordering_date = datetime.fromisoformat(i["startdate"])
			new_doc.receive_date =  datetime.fromisoformat(i["enddate"])
			new_doc.item = i["item"]
			new_doc.quantity =i["quantity"]
			new_doc.location = i["location"]
			new_doc.demand = demands[0]
			new_doc.insert()

		elif frappe.db.exists("Frepple Purchase Order", i["reference"]):
				frappe.db.set_value('Frepple Purchase Order', i["reference"], {
					'latest_reference': i["reference"],
					"ordering_date" : datetime.fromisoformat(i["startdate"]),
					"receive_date" :  datetime.fromisoformat(i["enddate"]),
					"quantity" : i["quantity"],
					"status" : i["status"],
					"supplier" : i["supplier"],
					"location" : i["location"],
				})

''' Draft
	for i in data:
		pos = frappe.db.sql(
			"""
			SELECT name,item,supplier
			FROM `tabFrepple Purchase Order`
			WHERE item = %s and supplier = %s
			""",
		[i["item"],i["supplier"]],as_dict=1)
		print (pos)
		if len(pos) == 0:
		# if not frappe.db.exists("Frepple Purchase Order",i["reference"]):
			new_doc = frappe.new_doc("Frepple Purchase Order")
			new_doc.reference = i["reference"]
			new_doc.latest_reference = i["reference"]
			new_doc.supplier = i["supplier"]
			new_doc.status = i["status"]
			new_doc.ordering_date = datetime.fromisoformat(i["startdate"])
			new_doc.receive_date =  datetime.fromisoformat(i["enddate"])
			new_doc.item = i["item"]
			new_doc.quantity =i["quantity"]
			new_doc.insert()
			#print(new_doc.name)
		else: #update
			existing_doc = frappe.get_doc("Frepple Purchase Order",pos[0].name)
			frappe.db.set_value('Frepple Purchase Order', pos[0].name, #Update the status
			{
				'latest_reference': i["reference"],
				"ordering_date" : datetime.fromisoformat(i["startdate"]),
				"receive_date" :  datetime.fromisoformat(i["enddate"]),
				"quantity" : i["quantity"]
			})
'''


def import_distribution_order():		
	api = "distributionorder"
	
	''' With filtering'''
	# filter = "?name=SAL-ORDER-0002"
	# filter = None
	# filter = "?status__contain=open"
	# url,headers = get_frepple_params(api=None,filter=filter)
	#filter = "?status=proposed"
	
	url,headers = get_frepple_params(api=api,filter=None)
	output = make_get_request(url,headers=headers)

	return output

def generate_distribution_order(data):
	for i in data:
		#print(i)
		#print("_______________________________________")
		demands = list(i["plan"]["pegging"].keys())
		#resource_list = list(i["resources"])
		resource_list = []

		if not frappe.db.exists("Frepple Distribution Order", i["reference"]):
			new_doc = frappe.new_doc("Frepple Distribution Order")
			new_doc.reference = i["reference"]
			new_doc.item = i["item"]
			new_doc.origin = i["origin"]
			new_doc.destination = i["destination"]
			new_doc.quantity = i["quantity"]
			new_doc.status = i["status"]
			new_doc.shipping_date = datetime.fromisoformat(i["startdate"])
			new_doc.receipt_date =  datetime.fromisoformat(i["enddate"])
			new_doc.demand = demands[0]
			for resource in resource_list:
				new_doc.append('resource', {
					'reference': i["reference"],
					'resource': resource["resource"],
					'resource_quantity': resource["quantity"]
				})
			new_doc.insert()

		elif frappe.db.exists("Frepple Distribution Order", i["reference"]):
				frappe.db.set_value('Frepple Distribution Order', i["reference"], {
					'item' : i["item"],
					'origin': i["origin"],
					'status': i["status"],
					'demand' : demands[0],
					'quantity': i["quantity"],
					'shipping_date': datetime.fromisoformat(i["startdate"]),
					'receipt_date': datetime.fromisoformat(i["enddate"])
 				}) 

	''' Draft
		demands = list(i["plan"]["pegging"].keys())
		
		#check_value = i["origin"]+' > '+i["destination"]+' | '+i["startdate"]+' / '+i["enddate"]+' | '+demands[0]
		#check_list = []

		#if check_value not in check_list:
		#if not frappe.db.exists("Frepple Distribution Order", i["origin"]+'>'+i["destination"]+'|'+i["startdate"]+'/'+i["enddate"]+'|'+demands[0]):
		if not frappe.db.exists("Frepple Distribution Order", i["origin"]+"-To-"+i["destination"]+"-At-"+i["startdate"]+"-"+i["enddate"]):
			#check_list.append(check_value)
			new_list =[]
			for j in data:
				if (i["reference"] != j["reference"])&(i["origin"] == j["origin"])&(i["destination"] == j["destination"])&(i["startdate"] == j["startdate"])&(i["enddate"] == j["enddate"]):
					new_list.append(i) if i not in new_list else new_list
					new_list.append(j) if j not in new_list else new_list
				else:
					new_list.append(i) if i not in new_list else new_list
			new_doc = frappe.new_doc("Frepple Distribution Order")
			new_doc.origin = i["origin"]
			new_doc.destination = i["destination"]
			new_doc.status = i["status"]
			new_doc.shipping_date = datetime.fromisoformat(i["startdate"])
			new_doc.receipt_date =  datetime.fromisoformat(i["enddate"])
			new_doc.demand = demands[0]
			for item in new_list:
				new_doc.append('item', {
					'reference': item["reference"],
					'material': item["item"],
					'material_quantity': item["quantity"]
				})
			new_doc.insert()	
		#elif frappe.db.exists("Frepple Distribution Order", i["origin"]+'>'+i["destination"]+'|'+i["startdate"]+'/'+i["enddate"]+'|'+demands[0]):
	'''


