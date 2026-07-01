import logging
from cli.arguments import create_parse
from utils.validator import validate_target
from utils.config import load_config
from utils.logger import setup_logger

logger = logging.getLogger(__name__)
def main():
    setup_logger()
    logging.info("Iniciando Aplicação")
    print("Ferramente De Reconhecimento De rede Iniciando....")
    config = load_config()
    print (config) 

    parser = create_parse()
    args = parser.parse_args()

    try:
        target_validado = validate_target(args.target)
        logging.info("Target validado com sucesso")
        print("Alvo:", target_validado)
        print("Varredura:", args.scan)
        
    except ValueError as erro:
        print (f"Erro: {erro}")

        logging.info("Aplicação finalizada")

if __name__ == "__main__":

    main()
