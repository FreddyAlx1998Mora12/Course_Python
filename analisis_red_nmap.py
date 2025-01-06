import nmap

# PortScanner -> clase para analisis de puertos de red
# scanner literalmente sera un objeto o una clase de PortScanner
scanner = nmap.PortScanner()

ip = input("Ingrese su direccion IP... revise su direccion ip con ipconfig..")

print("Su direccion IP ingresada es : ",ip)

# Scanearemos la ip, usand la clase PortScanner
scanner.scan(ip)
# imprimiremos las ips scaneado
print(scanner.all_hosts)
