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
	    _("ID") + ":Link/Commodity:180",
	    _("No.Permohonan") + ":Data:180",
		_("Tgl.Permohonan")+ ":Date:120",
		_("Nama Pengirim")+ ":Data:250",
		_("Alamat Pengirim")+ ":Data:120",
		_("Nama Penerima")+ ":Data:250",
		_("Alamat Penerima")+ ":Data:120",
		_("Jumlah Kemasan")+ ":Data:120",
		_("Asal")+ ":Data:200",
		_("Pelabuhan Asal")+ ":Data:220",
		_("Pelabuhan Tujuan")+ ":Data:180",
		_("Nama Alat Angkut")+ ":Data:180",
		_("Periksa")+ ":Data:120",
		_("Tujuan Pengeluaran Pemasukan")+ ":Data:120",
		_("Tempat Periksa Karantina")+ ":Data:220",
		_("Nama Komoditas")+ ":Data:120",
		_("Volume Bersih")+ ":Float:100",
		_("Satuan Bersih")+ ":Data:100",
		_("Kode HS")+ ":Data:100",
		_("Golongan")+ ":Data:80",
		_("Bentuk")+ ":Data:120",
		_("Jumlah Container")+ ":Data:120"
	]

def get_recheck_purchase_receipt(filters):
	conditions = get_conditions(filters)
	return frappe.db.sql(
		"""select
		        name,
				no_permohonan,
				tgl_permohonan,
				nama_pengirim,
				alamat_pengirim,
				nama_penerima,
				alamat_penerima,
				jumlah_kemasan,
				asal,
				pelabuhan_asal,
				pelabuhan_tujuan,
				nama_alat_angkut,
				periksa,
				tujuan_pengeluaran_pemasukan,
				tempat_periksa_karantina,
				nama_komoditas,
				vol_bersih,
				satuan_bersih,
				kode_hs,
				golongan,
				bentuk,
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
