# Copyright (c) 2013, molie and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	if not filters: filters = {}

	columns = get_columns()
	data = get_recheck_purchase_receipt(filters)

	return columns, data

def get_columns():
	return [
	    _("Nama Komoditas")+ ":Data:120",
	    _("Pelabuhan Asal")+ ":Data:220",
		_("Asal")+ ":Data:200",
		_("Jumlah Container")+ ":Data:120"
	]

def get_recheck_purchase_receipt(filters):
	conditions = get_conditions(filters)
	return frappe.db.sql(
		"""select
		        nama_komoditas,
		    	pelabuhan_asal,
				asal,
			    jumlah_kontainer				
		   from
		   		`tabCommodity`
		   where
		   		tujuan = 'INDONESIA' %s order by tgl_permohonan desc,no_permohonan desc
		""" % conditions, as_list=1)

def get_conditions(filters):
	conditions = ""

	if filters.get("from_date"):
		conditions += "and tgl_permohonan >= '%s'" % filters["from_date"]

	if filters.get("to_date"):
		conditions += "and tgl_permohonan <= '%s'" % filters["to_date"]

	return conditions
