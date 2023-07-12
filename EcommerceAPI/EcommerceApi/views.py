from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from .models import *
import json


# Create your views here.
class OrderView(APIView):
      def post(self, request):
        # data = json.loads(request.body)
        # order_items = data.get('items', [])
        order = Order.objects.create(users=request.user)
        # for order_item in order_items:
        #     item = Items.objects.get(id=order_item['item_id'])
        #     quantity = order_item['quantity']
        #     OrderItem.objects.create(order=order, item=item, quantity=quantity)
        # order.save()
        return JsonResponse({'status': 'success', 'order_id': order.id}, status=status.HTTP_201_CREATED)

class CartView(APIView):
    def post(self, request):
        order_id = request.data.get('order_id')
        item_id = request.data.get('item_id')
        quantity = int(request.data.get('quantity', 1))
        item = get_object_or_404(Items, id=item_id)
        order = get_object_or_404(Order, id=order_id, users=request.user)
        if quantity < 0:
            return JsonResponse({'error': 'Quantity cannot be negative.'}, status=status.HTTP_400_BAD_REQUEST)
        order_item = OrderItem.objects.create(order=order, item=item, quantity=quantity)
        return JsonResponse({'status': 'success', 'order_item_id': order_item.id}, status=status.HTTP_201_CREATED)
    
    def put(self, request):
        order_id = request.data.get('order_id')
        item_id = request.data.get('item_id')
        order_item = get_object_or_404(OrderItem, order__id=order_id, item__id=item_id, order__users=request.user)
        data = json.loads(request.body)
        quantity = data.get('quantity', order_item.quantity)
        if quantity < 0:
            return JsonResponse({'error': 'Quantity cannot be negative.'}, status=status.HTTP_400_BAD_REQUEST)
        order_item.quantity = quantity
        order_item.save()
        return JsonResponse({'status': 'success'}, status=status.HTTP_200_OK)

    def delete(self, request):
        order_id = request.data.get('order_id')
        item_id = request.data.get('item_id')
        order_item = get_object_or_404(OrderItem, order__id=order_id, item__id=item_id, order__users=request.user)
        order_item.delete()
