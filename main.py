import socket
import threading
import argparse
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import time

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP-Proxy"
}

def scan_port(target, port, timeout):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex((target, port))
        if result == 0:
            service = COMMON_PORTS.get(port, "Unknown")
            return port, True, service
        return port, False, None
    except socket.error:
        return port, False, None
    finally:
        sock.close()

def get_target_ip(target):
    try:
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror:
        print(f"Error: Couldn't resolve hostname '{target}'")
        return None

def port_scanner(target, port_range=(1, 1024), timeout=1.0, threads=100):
    ip = get_target_ip(target)
    if not ip:
        sys.exit(1)
    start_time = time.time()
    
    print(f"\n[*] Starting scan on {target} ({ip})")
    print(f"[*] Scanning {port_range[1] - port_range[0] + 1} ports from {port_range[0]} to {port_range[1]}")
    print(f"[*] Timeout set to {timeout} seconds")
    print(f"[*] Using {threads} threads")
    print(f"[*] Scan started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)
    
    open_ports = []
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        for port in range(port_range[0], port_range[1] + 1):
            futures.append(executor.submit(scan_port, ip, port, timeout))
        for future in futures:
            port, is_open, service = future.result()
            if is_open:
                open_ports.append((port, service))
    if open_ports:
        print(f"\n[+] Found {len(open_ports)} open ports:")
        for port, service in sorted(open_ports):
            print(f"    [+] Port {port}/tcp is open - {service}")
    else:
        print("\n[-] No open ports found")
    
    elapsed = time.time() - start_time
    print(f"\n[*] Scan completed in {elapsed:.2f} seconds")
    return open_ports

def main():
    parser = argparse.ArgumentParser(description="Network Port Scanner")
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument("-p", "--ports", help="Port range to scan (e.g., '1-1024')", default="1-1024")
    parser.add_argument("-t", "--timeout", type=float, help="Timeout in seconds", default=1.0)
    parser.add_argument("-T", "--threads", type=int, help="Number of threads", default=100)
    args = parser.parse_args()
  
    try:
        if "-" in args.ports:
            start_port, end_port = map(int, args.ports.split("-"))
        else:
            start_port = end_port = int(args.ports)
        if not (0 <= start_port <= 65535 and 0 <= end_port <= 65535):
            raise ValueError("Ports must be between 0 and 65535")
        if start_port > end_port:
            start_port, end_port = end_port, start_port
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    port_scanner(args.target, (start_port, end_port), args.timeout, args.threads)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Scan canceled by user")
        sys.exit(0)
