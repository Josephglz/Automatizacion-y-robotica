import asyncio
from bleak import BleakClient, BleakScanner

SERVICE_UUID = "12345678-1234-1234-1234-123456789abc"
CHARACTERISTIC_UUID = "abcdefab-cdef-abcd-efab-cdefabcdefab"

# Función para manejar notificaciones desde Arduino
def notification_handler(sender, data):
    print(f"Notificación desde {sender}: {data.decode('utf-8')}")

# Función para enviar mensajes desde Python al Arduino
async def send_message(client):
    while True:
        message = input("Ingresa un mensaje para enviar al Arduino: ")
        if message:
            await client.write_gatt_char(CHARACTERISTIC_UUID, message.encode('utf-8'))
        await asyncio.sleep(0.1)  # Evita bloquear el bucle de eventos

# Función principal que establece la conexión y maneja notificaciones
async def run():
    devices = await BleakScanner.discover()
    for device in devices:
        if device.name == "ArduinoBLE_Carrito":
            async with BleakClient(device.address) as client:
                # Conéctate y suscríbete a notificaciones
                await client.start_notify(CHARACTERISTIC_UUID, notification_handler)
                
                # Correr la función de envío de mensajes en paralelo
                await send_message(client)

# Ejecuta el bucle principal de asyncio
asyncio.run(run())


# import asyncio
# from bleak import BleakClient, BleakScanner

# SERVICE_UUID = "12345678-1234-1234-1234-123456789abc"
# CHARACTERISTIC_UUID = "abcdefab-cdef-abcd-efab-cdefabcdefab"

# # Función para manejar notificaciones
# def notification_handler(sender, data):
#     print(f"Notificación desde {sender}: {data.decode('utf-8')}")

# async def send_message(client):
#     while True:
#         message = input("Escribe un mensaje para enviar al Arduino (o 'exit' para salir): ")
#         if message.lower() == 'exit':
#             print("Cerrando conexión...")
#             break
#         # Envía el mensaje al Arduino
#         await client.write_gatt_char(CHARACTERISTIC_UUID, message.encode('utf-8'))

# async def run():
#     devices = await BleakScanner.discover()
#     for device in devices:
#         if device.name == "ArduinoBLE":
#             async with BleakClient(device.address) as client:
#                 print(f"Conectado a {device.name}")

#                 # Conéctate y suscríbete a notificaciones
#                 await client.start_notify(CHARACTERISTIC_UUID, notification_handler)
#                 print("Suscrito a notificaciones. Esperando mensajes...")

#                 # Corre la función de enviar mensajes en paralelo con la de recibir notificaciones
#                 send_task = asyncio.create_task(send_message(client))
                
#                 # Mantén la conexión indefinidamente para recibir notificaciones
#                 while True:
#                     await asyncio.sleep(1)  # Mantén el bucle corriendo

#                 await client.stop_notify(CHARACTERISTIC_UUID)
#                 await send_task

# asyncio.run(run())