import frappe

def get_context(context):
    context["company"] = frappe.db.sql("""SELECT company_name FROM tabCompany;""")[0][0]
    context['breadcrumb'] = "Home"
    context['title'] = "Home"
    context['page'] = "index.html"

    return context