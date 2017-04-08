# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "ea_theme"
app_title = "Ea Theme"
app_publisher = "Ebkar Technology & Management Solutions"
app_description = "Simple Website template, home, products, login, about, contact."
app_icon = "octicon octicon-browser"
app_color = "blue"
app_email = "info@ebkar.ly"
app_url = "https://github.com/imad-abdou/ea_theme"
app_license = "MIT"

# Includes in <head>
# ------------------
hide_in_installer = True
# include js, css files in header of desk.html
#app_include_css = ["/assets/ea_theme/css/ea_theme.css"]
#app_include_js = ["/assets/ea_theme/js/ea_theme.js"]

# include js, css files in header of web template
# web_include_css = "/assets/ea_theme/css/ea_theme.css"
# web_include_js = "/assets/ea_theme/js/ea_theme.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "index"



# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# website context
website_context = {
	"disable_website_theme": True
}

# Website user home page (by function)
# get_website_user_home_page = "ea_theme.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ea_theme.install.before_install"
# after_install = "ea_theme.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ea_theme.notifications.get_notification_config"

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
# 		"ea_theme.tasks.all"
# 	],
# 	"daily": [
# 		"ea_theme.tasks.daily"
# 	],
# 	"hourly": [
# 		"ea_theme.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ea_theme.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ea_theme.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ea_theme.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ea_theme.event.get_events"
# }

