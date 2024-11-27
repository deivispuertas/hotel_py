import asyncio
import random

async def process_payment(customer_name, amount):
    """Simula el procesamiento de un pago."""
    print(f'Procesado el pago de {customer_name} por $ {amount}...')
    await asyncio.sleep(random.randint(1,3))
    print(f'Pago de $ {amount} competada para {customer_name}')
    return True

