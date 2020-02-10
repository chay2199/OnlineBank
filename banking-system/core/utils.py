from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

def render_to_pdf(template_src):
    template = get_template(template_src)
    result = BytesIO()
    pdf = pisa.pisaDocument(result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None