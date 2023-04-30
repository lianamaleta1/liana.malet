import os
import sys

# Ruta a tu entorno virtual
VIRTUALENV_PATH = "/Documentos/Proyectos/api/myenv"

sys.path.append(os.path.join(VIRTUALENV_PATH, "lib", "python3.10.6", "site-packages"))

from fastapi import FastAPI

app=FastAPI()
# uvicorn main:app --reload

from typing import List

orders = [
    {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
    {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
    {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
    {"id": 4, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "canceled"}
]

criterion = 'completed'


def process_orders(orders: List[dict], criterion: str):
    filtered_orders = [order for order in orders if order['status'] == criterion]
   
    total_revenue = sum([order['quantity'] * order['price'] for order in filtered_orders if order['price'] > 0 and order['quantity'] >= 1 ])
    
    return total_revenue

total_revenue = process_orders(orders, criterion)
print(f'Total de ganancia para las {criterion} es de : {total_revenue}')
