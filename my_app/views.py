from django.shortcuts import render
from django.views.generic import View,ListView
from datetime import datetime
from .models import *
# Create your views here.


class OrdersView(View):
    def get(self, request):
        variable = 'Django'
        today_date = datetime.now()
        data = {
            'orders': [
                {'title': 'Первый заказ', 'id': 1},
                {'title': 'Второй заказ', 'id': 2},
                {'title': 'Третий заказ', 'id': 3}
            ]
        }
        return render(request, 'orders.html', locals())


class OrderView(View):
    def get(self, request, id):
        variable = 'Django'
        today_date = datetime.now()
        data = {
            'order': {
                'id': id
            }
        }
        return render(request, 'order.html', locals())


def main(request):
    return render(request, 'main.html', locals())


def db(request):
    return render(request, 'db.html', locals())


class BookView(ListView):
    model = Book
    template_name = 'books.html'


class WriterView(ListView):
    model = Writer
    template_name = 'writer.html'


def phone_info(request, id):
    name = ['iPhone 7', 'iPhone 8', 'iPhone X']
    ip7_info = 'В iPhone 7 все важнейшие аспекты iPhone значительно улучшены. Это принципиально новая система камер для фото и видеосъемки. Максимально мощный и экономичный аккумулятор. Стереодинамики с богатым звучанием. Самый яркий и разноцветный из всех дисплеев iPhone. Защита от брызг и воды. И его внешние данные впечатляют не менее, чем внутренние возможности. Все это iPhone 7. '
    ip8_info = 'Для iPhone 8 мы разработали совершенно новый дизайн, в котором передняя и задняя панели выполнены из стекла. Самая популярная камера усовершенствована. Установлен самый умный и мощный процессор, когда-﻿либо созданный для iPhone. Без проводов процесс зарядки становится элементарным. А дополненная реальность открывает невиданные до сих пор возможности. iPhone 8. Новое поколение iPhone.'
    ipX_info = 'Мы всегда мечтали сделать iPhone одним большим дисплеем. Настолько впечатляющим дисплеем, чтобы вы забывали о самом физическом устройстве. И настолько умным устройством, чтобы оно реагировало на прикосновение, слово и даже взгляд. iPhone X воплощает мечту в реальность. Это смартфон будущего.'
    info = [ip7_info, ip8_info, ipX_info]
    data1 = {'phone': {'id': id}}
    data2 = {'phones': [{'id': '1', 'phone_name': 'iPhone 7', 'info': ip7_info},
                       {'id': '2', 'phone_name': 'iPhone 8', 'info': ip8_info},
                       {'id': '3', 'phone_name': 'iPhone X', 'info': ipX_info}]}
    return render(request, 'phone_info.html', locals())

