import os

from django.db.models import Sum
from django.shortcuts import render
from transactions.models import Deposit, Withdrawal, Interest
from transfer.models import transfer
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


import pdfkit


def home(request):
    if not request.user.is_authenticated:
        return render(request, "core/home.html", {})
    else:
        user = request.user
        deposit = Deposit.objects.filter(user=user)
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
def generate_pdf(request):
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

        data = {
            "user": user,
            "transfer1": transfer1,
            "transfer2": transfer2,
            "deposit": deposit,
            "deposit_sum": deposit_sum,
            "withdrawal": withdrawal,
            "withdrawal_sum": withdrawal_sum,
            "interest": interest,
            "interest_sum": interest_sum,
        }
    path = os.getcwd()
    template = get_template(path + "/core/templates/core/transactions.html")
    context = data  # data is the context data that is sent to the html file to render the output.
    html = template.render(context)  # Renders the template with the context data.
    pdfkit.from_string(html, 'out.pdf')
    pdf = open("out.pdf")
    response = HttpResponse(pdf.read(), content_type='application/pdf')  # Generates the response as pdf response.
    response['Content-Disposition'] = 'attachment; filename=output.pdf'
    pdf.close()
    os.remove("out.pdf")  # remove the locally created pdf file.
    return response  # returns the response.
