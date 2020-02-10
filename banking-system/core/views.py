from django.db.models import Sum
from django.shortcuts import render
from transactions.models import Diposit, Withdrawal, Interest
from transfer.models import transfer
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import HttpResponse
from django.template.loader import get_template, render_to_string
import pdfkit
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from fpdf import FPDF, HTMLMixin

from core.utils import render_to_pdf 


def home(request):
    if not request.user.is_authenticated:
        return render(request, "core/home.html", {})
    else:
        user = request.user
        deposit = Diposit.objects.filter(user=user)
        transfer1 = transfer.objects.filter(sender=user)
        transfer2 = transfer.objects.filter(receiver=user)
        deposit_sum = deposit.aggregate(Sum('amount'))['amount__sum']
        withdrawal = Withdrawal.objects.filter(user=user)
        withdrawal_sum = withdrawal.aggregate(Sum('amount'))['amount__sum']
        interest = Interest.objects.filter(user=user)
        interest_sum = interest.aggregate(Sum('amount'))['amount__sum']
        

        context = {
                    "user": user,
                    "transfer1":transfer1,
                    "transfer2":transfer2,
                    "deposit": deposit,
                    "deposit_sum": deposit_sum,
                    "withdrawal": withdrawal,
                    "withdrawal_sum": withdrawal_sum,
                    "interest": interest,
                    "interest_sum": interest_sum,
                  }

        return render(request, "core/transactions.html", context)


def about(request):
    return render(request, "core/about.html", {})


@login_required()
def GeneratePdf(request):
    # Use False instead of output path to save pdf to a variable
    projectUrl = request.get_host()
    pdf = pdfkit.from_url(projectUrl, False)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="transaction-report.pdf"'

    return response
