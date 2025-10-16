import socket
from datetime import datetime
import locale

# Gunakan format tanggal Indonesia (jika sistem mendukung)
try:
    locale.setlocale(locale.LC_TIME, 'id_ID.UTF-8')
except:
    # Jika sistem tidak punya locale Indonesia, tetap lanjut
    pass

# Konfigurasi server
SERVER_IP = '127.0.0.1'   # alamat server (localhost)
SERVER_PORT = 65432       # port server

# Membuat socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

print(f"Server UDP berjalan di {SERVER_IP}:{SERVER_PORT}")
print("Menunggu pesan dari client...\n")

while True:
    try:
        # Menerima pesan dari client
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode('utf-8')

        # Ambil waktu dan tanggal sekarang
        waktu_sekarang = datetime.now()

        # Format waktu dengan tanggal dan jam (contoh: Kamis, 16 Oktober 2025 - 13:45:22 WIB)
        waktu_format = waktu_sekarang.strftime("%A, %d %B %Y - %H:%M:%S WIB")

        # Tampilkan di terminal server
        print(f"[{waktu_format}] Pesan dari {client_address}: {message}")

        # Balasan untuk client
        reply = f"Pesan diterima oleh server pada {waktu_format}"
        server_socket.sendto(reply.encode('utf-8'), client_address)

    except KeyboardInterrupt:
        print("\nServer dihentikan oleh pengguna.")
        break
    except Exception as e:
        print(f"Terjadi error: {e}")
        break

# Tutup socket
server_socket.close()
print("Server ditutup.")
