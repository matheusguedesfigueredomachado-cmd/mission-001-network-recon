from cli.arguments import create_parse
from utils.validator import validate_target

def main():
    print("Ferramente De Reconhecimento De rede Iniciando....")

    parser = create_parse()
    args = parser.parse_args()

    try:
        target_validado = validate_target(args.target)

        print("Alvo:", target_validado)
        print("Varredura:", args.scan)
        
    except ValueError as erro:
        print (f"Erro: {erro}")


if __name__ == "__main__":
    main()
