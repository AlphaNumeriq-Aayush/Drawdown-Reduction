import argparse
from drawdown_redux_manager.utils import load_config, CustomFormatter
from drawdown_redux_manager.copier import CopyTradingService
from drawdown_redux_manager.streaming_api import run as run_stream
import dotenv
import asyncio
import os 


dotenv.load_dotenv()

DEBUG = False

def main():
    
    # Create the parser
    parser = argparse.ArgumentParser(description="Manage the copy trading service and the DDR algorithm.",
                                    formatter_class=CustomFormatter)

    subparsers = parser.add_subparsers(dest="command")
    subparsers.required = False

    copy_config_parser = subparsers.add_parser("copy-config",
                                            help="Set up copy trading service with a provided config.yaml file. Example usage: 'python main.py copy-config --config path/to/config.yaml'")
    copy_config_parser.add_argument("--config", 
                                    help="Provide path to the config.yaml file. Default: 'config.yaml'", 
                                    default="config.yaml")

    run_ddr_parser = subparsers.add_parser("run-ddr", 
                                        help="Run drawdown reduction algorithm on a specified account. Example usage: 'python main.py run-ddr --account account_name --config path/to/config.yaml'")
    run_ddr_parser.add_argument("--config", 
                                help="Provide path to the config.yaml file. Default: 'config.yaml'",
                                default="config.yaml")
    run_ddr_parser.add_argument("--account", 
                                help="Provide name of the account to apply DDR. Required.",
                                required=True)

    args = parser.parse_args()

    # Load the config
    if args.command:
        config = load_config(args.config)
    else:
        config = load_config("config.yaml")

    # Execute the appropriate command
    if args.command == "copy-config":
        copy_trading_service = CopyTradingService(config, api_token=os.getenv("TOKEN"))
        asyncio.run(copy_trading_service.configure())
    elif args.command == "run-ddr":
        account_name = args.account
        run_stream(config, account_name)
    else:
        # This is debug mode and currently defaults to copy-config.
        if DEBUG:
            
            account_name = "EA_Signal_Pro_V5_Set3_Slave_Account"
            run_stream(config, account_name)
            
            #copy_trading_service = CopyTradingService(config, api_token=os.getenv("TOKEN"))
            #asyncio.run(copy_trading_service.configure())

if __name__ == "__main__":

    main()