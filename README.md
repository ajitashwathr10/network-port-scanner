# Network Port Scanner
A fast, multi-threaded network port scanner built in Python. This tool scans target systems for open ports and identifies common services running on those ports.

## Features

- 🚀 **Multi-threaded scanning** for high performance
- 🎯 **Flexible targeting** - scan any hostname or IP address
- 🔍 **Custom port ranges** - scan specific port ranges
- ⏱️ **Adjustable timeouts** - customize connection timeout values
- 🔎 **Service identification** - recognizes common services on standard ports
- 💪 **Lightweight** - zero external dependencies

## Installation
This tool uses only Python standard library modules, so no additional installation is needed beyond Python itself.

```bash
# Clone the repository or download port_scanner.py
git clone https://github.com/ajitashwathr10/network-port-scanner.git
cd port-scanner

# Make the script executable (Linux/Mac)
chmod +x port_scanner.py
```

## Usage

```bash
python port_scanner.py TARGET [options]
```

### Command Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `TARGET` | Target IP address or hostname (required) | - |
| `-p`, `--ports` | Port range to scan (e.g., '1-1024') | 1-1024 |
| `-t`, `--timeout` | Connection timeout in seconds | 1.0 |
| `-T`, `--threads` | Number of threads to use | 100 |

### Examples

Scan the default ports on a domain:
```bash
python port_scanner.py example.com
```

Scan a specific port range on an IP address:
```bash
python port_scanner.py 192.168.1.1 -p 20-80
```

Scan with a faster timeout and more threads:
```bash
python port_scanner.py 10.0.0.1 -p 1-10000 -t 0.5 -T 200
```

## Sample Output

```
[*] Starting scan on example.com (93.184.216.34)
[*] Scanning 1024 ports from 1 to 1024
[*] Timeout set to 1.0 seconds
[*] Using 100 threads
[*] Scan started at 2025-05-16 14:30:27
------------------------------------------------------------

[+] Found 2 open ports:
    [+] Port 80/tcp is open - HTTP
    [+] Port 443/tcp is open - HTTPS

[*] Scan completed in 5.26 seconds
```

## Important Note
⚠️ Only use this tool on systems you own or have explicit permission to scan. Unauthorized port scanning may be illegal in some jurisdictions.

## Expanding the Tool
Here are some ideas for extending the port scanner:
- Add service version detection
- Implement OS fingerprinting
- Add output formats (JSON, CSV, etc.)
- Create a GUI interface
- Add detailed vulnerability checking
