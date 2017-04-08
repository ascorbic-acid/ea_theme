import frappe

def get_context(context):
    context["company"] = frappe.db.sql("""SELECT company_name FROM tabCompany;""")[0][0]
    context['breadcrumb'] = "Products"
    context['title'] = 'Products'
    context['page'] = 'products.html'

    return context