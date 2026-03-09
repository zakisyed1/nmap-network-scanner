import nmap

scanner = nmap.PortScanner()

target = input("Enter network range (example: 192.168.1.0/24): ")

print(f"\nScanning {target}...\n")

scanner.scan(hosts=target, arguments='-sn')

print("Active devices:\n")

for host in scanner.all_hosts():
    print(f"Device found: {host}")
