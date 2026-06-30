from cli.arguments import create_parse

def main():
    print("Ferramente De Reconhecimento De rede Iniciando....")

    parser = create_parse()

    args = parser.parse_args()

    print("Alvo:", args.target)
    print("Varredura:", args.scan)


if __name__ == "__main__":
    main()
