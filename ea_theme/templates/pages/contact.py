import frappe

def get_context(context):
    context["company"] = frappe.db.sql("""SELECT company_name FROM tabCompany;""")[0][0]
    context['breadcrumb'] = "Contact Us"
    context['title'] = 'Contact Us'
    context['page'] = 'contact.html'

    return context