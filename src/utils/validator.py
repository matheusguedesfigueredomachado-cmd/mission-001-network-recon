from ipaddress import ip_address, ip_network

def validate_target(target: str):
    try:
        return ip_network(target, strict=False)
    except ValueError:
        try:
            return ip_address(target)
        except ValueError:
            raise ValueError(
                f"Target Inválido: '{target}'. "
                "Forneça um endereço IP válido ou um código CIDR para a rede."
            )