import socket

target = input("Enter target IP or hostname: ")

print(f"\nScanning {target}...\n")

for port in range(1, 1025):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is OPEN")

        sock.close()

    except KeyboardInterrupt:
        print("\nScan stopped by user.")
        break

    except socket.gaierror:
        print("Hostname could not be resolved.")
        break

    except socket.error:
        print("Could not connect to server.")
        break