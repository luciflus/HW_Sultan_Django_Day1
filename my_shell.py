python manage.py shell
from shop.models import Item, Purchase
q = Item.objects.create(name="Телевизор", price=70000)
q.save()
q.purchases.create(name="Sultan", age=30, date_purchase='03.12.2022')
q.purchases.create(name="Бек", age=23, date_purchase='11.11.2022')
q.purchases.create(name="Олег", age=45, date_purchase='11.20.2022')

q = Item.objects.create(name="Микроволновка", price=5000)
q.save()
q.purchases.create(name="Дмитрий", age=45, date_purchase='11.20.2022')
q.purchases.create(name="Олег", age=45, date_purchase='11.20.2022')

q = Item.objects.create(name="Стиральная машина", price=30000)
q.save()
q.purchases.create(name="Sultan", age=30, date_purchase='03.12.2022')
q.purchases.create(name="Олег", age=45, date_purchase='11.20.2022')

q = Item.objects.create(name="Фен", price=2000)
q.save()
q.purchases.create(name="Arina", age=19, date_purchase='31.12.2022')

q = Item.objects.create(name="Музыкальный центр", price=15000)
q.save()
q.purchases.create(name="Айбек", age=25, date_purchase='01.01.2022')
q.purchases.create(name="Евгений", age=35, date_purchase='01.01.2022')

q = Item.objects.create(name="Принтер", price=15000)
q.save()
q.purchases.create(name="Sultan", age=30, date_purchase='03.12.2022')

q = Item.objects.create(name="Монитор", price=15000)
q.save()
q.purchases.create(name="Sultan", age=30, date_purchase='03.12.2022')
q.purchases.create(name="Евгений", age=35, date_purchase='01.01.2022')

q = Item.objects.create(name="Органайзер", price=1500)
q.save()
q.purchases.create(name="Sultan", age=30, date_purchase='03.12.2022')

q = Item.objects.create(name="Клавиатура", price=1500)
q.save()
q.purchases.create(name="Sultan", age=30, date_purchase='03.12.2022')
q.purchases.create(name="Айбек", age=25, date_purchase='01.01.2022')
q.purchases.create(name="Бек", age=23, date_purchase='01.01.2022')

q = Item.objects.create(name="Мышка", price=1500)
q.save()
q.purchases.create(name="Sultan", age=30, date_purchase='03.12.2022')
q.purchases.create(name="Айбек", age=25, date_purchase='01.01.2022')
q.purchases.create(name="Бек", age=23, date_purchase='01.01.2022')

exit()