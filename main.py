import socket

def check_ports(target_host, start_port, end_port, timeout=1.0):
    print(f"\nScanning host: {target_host}")
    print(f"{'PORT':<10}{'STATUS':<15}{'SERVICE/NOTES':<20}")
    print("-" * 45)

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
            result = s.connect_ex((target_host, port))
            if result == 0:
                print(f"{port:<10}{'OPEN':<15}{'Service active':<20}")
            else:
                print(f"{port:<10}{'CLOSED':<15}{'No response/Closed':<20}")
        except socket.timeout:
            print(f"{port:<10}{'FILTERED':<15}{'Connection timed out':<20}")
        except Exception as e:
            print(f"{port:<10}{'ERROR':<15}{str(e):<20}")
        finally:
            s.close()

if __name__ == "__main__":
    target = input("Enter target IP/Host (e.g., scanme.nmap.org or 127.0.0.1): ").strip()
    start_p = int(input("Enter start port (e.g., 20): "))
    end_p = int(input("Enter end port (e.g., 85): "))
    
    check_ports(target, start_p, end_p)
  
