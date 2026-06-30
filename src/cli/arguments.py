from argparse import ArgumentParser

def create_parse() ->ArgumentParser:
    
    parser = ArgumentParser(
        description="Ferramenta Profissional De Reconhecimento De Rede"
    )

    parser.add_argument(
        "--target",
        required=True,
        help="Endereço IP ou rede CIDR alvo."
    )

    parser.add_argument (
        "--scan",
        choices=["host","tcp"],
        required=True,
        help="Tipo de Varredura a Ser Executada"
    )

    return parser