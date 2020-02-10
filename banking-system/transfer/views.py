# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
from django.core.validators import MinValueValidator
from .forms import TransferForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect


User = settings.AUTH_USER_MODEL

# Create your views here.
@login_required()
def transfer_fund(request):
    form = TransferForm(request.POST or None)
    if form.is_valid():

	    transfer = form.save(commit=False)
	    transfer.sender = request.user
	    receiver_data= transfer.receiver
	    email=form.cleaned_data.get("receiver")
	    transfer.receiver=email
	    transfer.amount=form.cleaned_data.get("amount")
	    transfer.save()
	    if transfer.sender.account.balance<transfer.amount:
	    	messages.success(
            request, 'You cannot Withdraw more than your balance {} $.'.format(transfer.amount)
        	)
        	return redirect("home")
	        # adds users deposit to balance.
	    transfer.sender.account.balance -= transfer.amount
	    transfer.receiver.account.balance += transfer.amount
	    transfer.sender.account.save()
	    transfer.receiver.account.save()
	    messages.success(request, 'You Have Deposited {} $.'
	                         .format(transfer.amount))
	    return redirect("home")

    context = {
        "title": "Fund Transfer",
        "form": form
    }
    return render(request, "transfer_fund.html", context)
