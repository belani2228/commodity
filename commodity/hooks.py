# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "commodity"
app_title = "Commodity"
app_publisher = "lukptr"
app_description = "App Commodity"
app_icon = "octicon octicon-package"
app_color = "#a1f488"
app_email = "lukptr@yahoo.com"
app_license = "ABC GROUPS"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/commodity/css/commodity.css"
# app_include_js = "/assets/commodity/js/commodity.js"

# include js, css files in header of web template
# web_include_css = "/assets/commodity/css/commodity.css"
# web_include_js = "/assets/commodity/js/commodity.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "commodity.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "commodity.install.before_install"
# after_install = "commodity.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "commodity.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"commodity.tasks.all"
# 	],
# 	"daily": [
# 		"commodity.tasks.daily"
# 	],
# 	"hourly": [
# 		"commodity.tasks.hourly"
# 	],
# 	"weekly": [
# 		"commodity.tasks.weekly"
# 	]
# 	"monthly": [
# 		"commodity.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "commodity.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "commodity.event.get_events"
# }

