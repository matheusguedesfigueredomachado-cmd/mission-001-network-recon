import logging
from cli.arguments import create_parse
from utils.validator import validate_target
from utils.config import load_config
from utils.logger import setup_logger
from core.engine import execute_scan 

logger = logging.getLogger(__name__)

def main():
    setup_logger()
    logger.info("Application started")

    print("Ferramenta De Reconhecimento De rede Iniciando....")

    config = load_config()
   

    parser = create_parse()
    args = parser.parse_args()

    try:
        
        target_validado = validate_target(args.target)
        logger.info(f"Target validated successfully: {target_validado}")

        
        target_str = str(target_validado)

        print(f"Iniciando varredura do tipo '{args.scan}' em: {target_str}")
        logger.info(f"Starting {args.scan} scan")

        
        resultados = execute_scan(target=target_str, scan_type=args.scan)

        print("\nHosts ativos encontrados:")
        print(resultados)
        logger.info(f"Scan finished. Found {len(resultados)} hosts.")
        
    except ValueError as erro:
        logger.error(f"Validation failed: {erro}")
        print(f"Erro: {erro}")
    except Exception as erro_inesperado:
        
        logger.error(f"Unexpected error: {erro_inesperado}")
        print(f"Erro inesperado durante a execução: {erro_inesperado}")

    logger.info("Application finished")

if __name__ == "__main__":
    main()