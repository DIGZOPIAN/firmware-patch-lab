import asyncio
from bleak import BleakClient

# BLE device MAC or UUID
DEVICE_UUID = "AC19D108-D399-028D-137C-30BBE452C7FD"

# Nordic UART-style characteristic UUIDs
SERVICE_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
WRITE_CHAR_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
NOTIFY_CHAR_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"

# Load firmware patch (binary mode)
FIRMWARE_PATH = "custom_patch.bin"  # Must be in same directory

CHUNK_SIZE = 20

async def run():
    async with BleakClient(DEVICE_UUID) as client:
        print(f"[+] Connected to {DEVICE_UUID}")

        def handle_notify(sender, data):
            print(f"[<] {data.hex()}")

        await client.start_notify(NOTIFY_CHAR_UUID, handle_notify)

        with open(FIRMWARE_PATH, "rb") as fw:
            firmware = fw.read()

        print(f"[>] Sending firmware patch ({len(firmware)} bytes)...")
        for i in range(0, len(firmware), CHUNK_SIZE):
            chunk = firmware[i:i+CHUNK_SIZE]
            await client.write_gatt_char(WRITE_CHAR_UUID, chunk)
            await asyncio.sleep(0.05)  # Tune this delay if needed

        print("[✓] Firmware patch sent.")
        await client.stop_notify(NOTIFY_CHAR_UUID)

asyncio.run(run())
