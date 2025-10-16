import socket

# Konfigurasi client
SERVER_IP = '127.0.0.1'  # alamat server (localhost)
SERVER_PORT = 65432      # port server

# Membuat socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Input pesan dari pengguna
    message = input("Ketik pesan untuk server: ")

    # Kirim pesan ke server
    client_socket.sendto(message.encode('utf-8'), (SERVER_IP, SERVER_PORT))

    # Terima balasan dari server
    data, addr = client_socket.recvfrom(1024)
    print(f"Balasan dari server: {data.decode('utf-8')}")

except Exception as e:
    print(f"Terjadi error: {e}")

finally:
    # Tutup koneksi socket
    client_socket.close()
