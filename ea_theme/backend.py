from __future__ import unicode_literals
import frappe

@frappe.whitelist(allow_guest=True)
def query(uid):
    re = frappe.db.sql("""SELECT user_type FROM tabUser WHERE name='{0}'""".format(uid))
    
    return re