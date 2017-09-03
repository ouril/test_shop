from django.shortcuts import render
from django.db import transaction
from .models import UserBalance, UserBalanceChange
from shop.models import Product

# open a transaction
#@transaction.atomic
def buy(request, pk):
    print(pk)
    product = Product.objects.get(pk=pk)
    user = request.user.id
    print(user)
    new_change = UserBalance.objects.get(
            pk=user
    )
    print(product)
    print(new_change)


    
#  a.save()
    # transaction now contains a.save()

   # sid = transaction.savepoint()  

   # b.save()
    # transaction now contains a.save() and b.save()

  #  if want_to_keep_b:
  #      transaction.savepoint_commit(sid)
        # open transaction still contains a.save() and b.save()
  #  else:
  #      transaction.savepoint_rollback(sid)
        # open transaction now contains only a.save()
# Create your views here.
