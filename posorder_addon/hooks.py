from . import __version__ as app_version

app_name = "posorder_addon"
app_title = "Posorder Addon"
app_publisher = "Jide Olayinka"
app_description = "Creating Sales Invoice Order helper"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "olajamesjide@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/posorder_addon/css/posorder_addon.css"
# app_include_js = "/assets/posorder_addon/js/posorder_addon.js"

# include js, css files in header of web template
# web_include_css = "/assets/posorder_addon/css/posorder_addon.css"
# web_include_js = "/assets/posorder_addon/js/posorder_addon.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "posorder_addon/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "posorder_addon.install.before_install"
# after_install = "posorder_addon.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "posorder_addon.uninstall.before_uninstall"
# after_uninstall = "posorder_addon.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "posorder_addon.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Invoice": {
        "on_update": "posorder_addon.posorder_addon.utils.make_sales_order",
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"posorder_addon.tasks.all"
# 	],
# 	"daily": [
# 		"posorder_addon.tasks.daily"
# 	],
# 	"hourly": [
# 		"posorder_addon.tasks.hourly"
# 	],
# 	"weekly": [
# 		"posorder_addon.tasks.weekly"
# 	]
# 	"monthly": [
# 		"posorder_addon.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "posorder_addon.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "posorder_addon.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "posorder_addon.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"posorder_addon.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
