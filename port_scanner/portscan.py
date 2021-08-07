import asyncio
import argparse
import socket
import subprocess
from typing import List
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import colorama

pbar = tqdm(total = 65536, colour = "red")

def scan_port(ip: str, port: int, is_verbose: bool = False) -> bool:
    global pbar
    if is_verbose: pbar.update(1)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((ip, port))
            return True
        except:
            return False

def get_open_ports(ip: str, timeout: int, is_verbose: bool = False) -> List[int]:
    open_ports = []
    socket.setdefaulttimeout(timeout)
    with ThreadPoolExecutor(max_workers=500) as executor:
        for port, is_open in enumerate(executor.map(lambda port: scan_port(ip, port, is_verbose=is_verbose), range(65536))):
            if is_open:
                open_ports.append(port)
                print(colorama.Fore.GREEN + f"[✓] Port {port} open!" + colorama.Style.RESET_ALL)
    return open_ports


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Simple (accelerated) port scanner with nmap support")
    parser.add_argument("ip", metavar = "ip", type = str, help = "IP to be scanned")
    parser.add_argument("-t", metavar = "timeout", type = int, default = 2, help = "Timeout (s)")
    parser.add_argument("-n", dest = "nmap", action = "store_true", default=False, help = "Enable if you want to run nmap on found ports")
    parser.add_argument("-v", dest = "verbose", action = "store_true", default=False, help = "Enable if you want to have progress bar")
    args = parser.parse_args()
    print(colorama.Fore.LIGHTMAGENTA_EX + "[x] Scanning ports..." + colorama.Style.RESET_ALL)
    open_ports = get_open_ports(args.ip, args.t, is_verbose = args.verbose)
    if args.nmap:
        print(colorama.Fore.LIGHTMAGENTA_EX + "[x] Running nmap command")
        subprocess.call(f"nmap -sC -sV -oA nmap_output -p {''.join([str(i) for i in open_ports])}",shell=True)

