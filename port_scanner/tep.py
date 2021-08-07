import asyncio

async def scan_port(ip, port, timeout):
    # Some code taken from https://stackoverflow.com/questions/35543955/python3-5-asyncio-tcp-scanner
    print(f"Port: {port}")
    try:
        connection = asyncio.open_connection(ip, port)
        reader, writer = await asyncio.wait_for(connection, timeout=timeout)
        print(f"Port {port} is open!")
    except:
        print(f"Port {port} is closed!")


if __name__ == "__main__":
#    parser = argparse.ArgumentParser(description = "Simple (accelerated) port scanner with nmap support")
#    parser.add_argument("ip", metavar = "ip", type = str, help = "IP to be scanned")
#    parser.add_argument("-t", metavar = "timeout", type = int, help = "Timeout (s)")
#    parser.add_argument("-n", dest = "nmap", action = "store_true", default=False, help = "")
#    args = parser.parse_args()
#    print(args)
#    asyncio.run(scan_ip("scanme.nmap.org", timeout=5))
    asyncio.run(scan_port("scanme.nmap.org", 70, 5))
