from django.shortcuts import render
from django.db import transaction
from django.shortcuts import render
from .models import (
    UserBalance, 
    UserBalanceChange
)
from shop.models import (
    Product, 
    Store,
    Order
    )


def buy(request, pk):
    """Function for making order and balance changes
       Use transactions
    """
    store = Store.objects.get(id=pk)
    price = store.product.price
    print(store.number)
    if store.number < 0:
        return render(request, 'response.html', 
    {
        'message':"Товара нет на складе"
        })
    store.number = store.number - 1
    user = request.user
    new_change = UserBalance.objects.get(pk=user.id)    
    balance = new_change.balance
    if balance < price:
        return render(request, 'response.html', 
    {
        'message':"Недостаточно средств"                     
        })
    else:
        new_change.balance = balance - price
        balance_change = UserBalanceChange(
                user=user,
                amount=price,
                reason="Заказ " + str(store.product.name)
            )
        order = Order(
                user=user,
                product=store.product,
                number=1
            )
        try:
            with transaction.atomic():
                order.save()
                new_change.save()
                store.save()
                balance_change.save()
        except:
            return render(request, 'response.html', 
    {
        'message':"Произошла ошибка! Транзакция не выполнена"                     
        })

        return render(request, 'response.html', 
    {
        'message':"Покупка совершена успешно",
        })

