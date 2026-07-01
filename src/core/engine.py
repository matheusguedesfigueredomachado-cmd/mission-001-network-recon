from scanners.host_discovery import discover_hosts

def execute_scan(target: str, scan_type: str):

    if scan_type == "host":
        return discover_hosts(target)

    raise ValueError("Tipo de varredura não suportado.")