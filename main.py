import random
import webbrowser
import requests

def ascii_art():
    art = """
███████╗ ██████╗ ██╗██████╗ ██╗         ██╗  ██╗██╗██╗     ██╗     ███████╗██████╗ 
██╔════╝██╔════╝ ██║██╔══██╗██║         ██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗
█████╗  ██║  ███╗██║██████╔╝██║         █████╔╝ ██║██║     ██║     █████╗  ██████╔╝
██╔══╝  ██║   ██║██║██╔══██╗██║         ██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗
███████╗╚██████╔╝██║██║  ██║███████╗    ██║  ██╗██║███████╗███████╗███████╗██║  ██║
╚══════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
    """
    return art

def ip_tracking(ip):
    print(f"\033[91mTracking IP: {ip}\033[0m")
    print(f"\033[91mLocation: {random.choice(['USA', 'Europe', 'Asia', 'Australia'])}\033[0m")

def route_tracing(ip):
    print(f"\033[91mTracing route for IP: {ip}\033[0m")
    for i in range(1, 6):
        print(f"{i}  {random.randint(1, 100)}ms")

def ddos_simulation(ip):
    print(f"\033[91mDDoS attack on IP: {ip}\033[0m")
    while True:
        print("\033[91m Sending requests...\033[0m")

def ip_spoofing(target_ip):
    print(f"\033[91IP Spoofing on: {target_ip}\033[0m")
    print(f"Attacking from: {random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}")

def port_scanning(target_ip):
    print(f"\033[91mScanning ports on IP: {target_ip}\033[0m")
    ports = random.sample(range(1, 65536), 10)
    print(f"\033[91mOpen ports: {ports}\033[0m")

def vulnerability_scanning(target_ip):
    print(f"\033[91mScanning for vulnerabilities on: {target_ip}\033[0m")
    vulnerabilities = random.sample(['SQL Injection', 'XSS', 'CSRF', 'File Inclusion'], 2)
    print(f"\033[91mFound vulnerabilities: {vulnerabilities}\033[0m")

def swat_command():
    print(f"\033[91mExecuting SWAT Command...\033[0m")
    print(f"\033[91mRedirecting to FBI.gov...\033[0m")
    webbrowser.open('https://www.fbi.gov')
    print(f"\033[91mNavigating to FBI.gov...\033[0m")
    print(f"\033[91mConnection established with FBI servers.\033[0m")
    print(f"\033[91mPlease wait for further instructions...\033[0m")

def info_gathering(username):
    print(f"\033[91mGathering information for user: {username}\033[0m")
    webbrowser.open(f"https://pipl.com/search/{username}")
    webbrowser.open(f"https://www.spokeo.com/{username}")
    webbrowser.open(f"https://www.intelius.com/results.php?ReportType=1&Ntt={username}")

def main():
    print(ascii_art())
    print("\033[91mSimple Dox Tool\033[0m")

    while True:
        print("\n――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        print("\033[91mChoose an option:\033[0m")
        print("1  -  IP Tracking      |  4  -  IP Spoofing")
        print("2  -  Route Tracing    |  5  -  Port Scanning")
        print("3  -  DDoS Simulation  |  6  -  Vulnerability Scanning")
        print("7  -  Info Gathering   |  8  -  SWAT Command")
        print("9  -  Exit")
        print("\n____________________________________________________________________________________________________________________")

        choice = input("\n\033[91mEnter your choice: \033[0m")

        if choice == '1':
            ip = input("\033[91mEnter IP to track: \033[0m")
            ip_tracking(ip)
        elif choice == '2':
            ip = input("\033[91mEnter IP for route tracing: \033[0m")
            route_tracing(ip)
        elif choice == '3':
            ip = input("\033[91mEnter IP for DDoS Attack: \033[0m")
            ddos_simulation(ip)
        elif choice == '4':
            target_ip = input("\033[91mEnter target IP for IP Spoofing: \033[0m")
            ip_spoofing(target_ip)
        elif choice == '5':
            target_ip = input("\033[91mEnter target IP for Port Scanning: \033[0m")
            port_scanning(target_ip)
        elif choice == '6':
            target_ip = input("\033[91mEnter target IP for Vulnerability Scanning: \033[0m")
            vulnerability_scanning(target_ip)
        elif choice == '7':
            username = input("\033[91mEnter username for info gathering: \033[0m")
            info_gathering(username)
        elif choice == '8':
            swat_command()
        elif choice == '9':
            break
        else:
            print("\033[91mInvalid choice. Please try again.\033[0m")

if __name__ == "__main__":
    main()
