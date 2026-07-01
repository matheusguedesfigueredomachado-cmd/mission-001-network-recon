import nmap

def discover_hosts(target: str) -> list[str]:
   
    scanner = nmap.PortScanner()

   
    scanner.scan(hosts=target, arguments="-sn")

    
    return list(scanner.all_hosts())