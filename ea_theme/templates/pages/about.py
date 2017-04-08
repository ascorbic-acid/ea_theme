import frappe

def get_context(context):
    context["company_intro"] = frappe.get_doc("About Us Settings", None).company_introduction
    context["company"] = frappe.db.sql("""SELECT company_name FROM tabCompany;""")[0][0]
    context['breadcrumb'] = "About Us"
    context['title'] = 'About Us'
    context['page'] = 'about.html'

    return context