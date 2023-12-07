# Drawdown Reduction Manager

The Drawdown Reduction Manager is an application that manages a copy trading service and implements the Drawdown Reduction (DDR) algorithm. It allows you to configure and synchronize trades between multiple MetaTrader accounts, as well as reduce drawdowns using a streaming API.

## Prerequisites

Before using the Drawdown Reduction Manager, ensure that you have the following:

- MetaTrader accounts with the MetaApi provider
- MetaApi API token for accessing the MetaApi SDK and CopyFactory API
- Python 3.11 or above installed

## Installation

1. Clone the repository:
   ```shell
   git clone <repository_url>
   ```

2. Install the required dependencies:
   ```shell
   pip install -r requirements.txt
   ```

3. Set up your environment variables and configuration file:
   - Create a `.env` file in the root directory of the project.
   - Add the necessary environment variables in the `.env` file. You will need your MetaApi API token as well as login information and server names for each of your trading accounts. The prefix `<account_name>` should be replaced with the name of one of your slave accounts that you specify in the `config.yaml` file. This file is expandable, meaning you can add configuration information for multiple slave accounts like so:

     ```
     TOKEN=<your_metaapi_api_token>

     <account_name1>_LOGIN=<login1>
     <account_name1>_PASSWORD=<password1>
     <account_name1>_SERVER=<server1>

     <account_name2>_LOGIN=<login2>
     <account_name2>_PASSWORD=<password2>
     <account_name2>_SERVER=<server2>

     ...
     ```

     **Note**: Replace `<your_metaapi_api_token>`, `<account_name>`, `<login>`, `<password>`, and `<server>` with the corresponding values. The `<account_name>` must match one of the slave account names specified in the `config.yaml` file.

   - Configure your `config.yaml` file with the following structure:
     ```yaml
     # Copy Trading and Drawdown Reduction Configuration
     # Note you can only enable drawdown reduction on slave accounts. 
     masterAccounts:
       - id: <master_account_id>
         name: <master_account_name>
         description: <strategy_description>
         slaveAccounts: 
           - name: <slave_account_name> # Slave Account Name must be all one word
             id: <slave_account_id> # Meta API Account ID
             enable: true  # Enables copying for slave account
             multiplier: 1 # Trade Copier Multiplier
             symbolFilter:
               included: # Included Symbols for Slave Account
                 - <symbol1>
                 - <symbol2>
             allowedSides: # Allowed Sides for Slave Account
               - <side>
     ```
     **Note**: Replace `<master_account_id>`, `<master_account_name>`, `<strategy_description>`, `<slave_account_name>`, `<slave_account_id>`, `<symbol1>`, `<symbol2>`, and `<side>` with your actual values.

## How to Use

You can run the help command to get detailed instructions on how to use the application. 
```
python main.py --help
```

To execute your script from the command line, you can use the following command:

```
python main.py <command> --config <config_file_path> [--account <account_name>]
```

Replace `<command>` with either `copy-config` or `run-ddr`, depending on the desired action. The `--config` flag is optional and can be used to specify the path to the config file. If not provided, it will default to `"config.yaml"`. The `--account` flag is needed when running the drawdown reduction algorithm.

Here are a few examples:

- To configure the copy trading service with a specific config file:
  ```
  python main.py copy-config --config path/to/config.yaml
  ```

- To run the drawdown reduction algorithm on a specific account using a different config file:
  ```
  python main.py run-ddr --account <account_name> --config path/to/config.yaml
  ```

- To get the help documentation and see available options:
  ```
  python main.py -h
  ```

Make sure to replace `<repository_url>`, `<your_metaapi_api_token>`, `<config_file_path>`, and other placeholders with the appropriate values.

Remember to replace `path/to/config.yaml` or `path/to/another_config.yaml` with the actual paths to your config files.

## Disclaimer

The Drawdown Reduction Manager is a software application provided as-is, without any warranties or guarantees of any kind. By using this application, you acknowledge and agree that:

1. **No Financial Advice**: The Drawdown Reduction Manager does not provide financial or investment advice. It is your responsibility to perform your own research, analysis, and decision-making regarding your trades and investments.

2. **Use at Your Own Risk**: Trading in the financial markets carries inherent risks. The use of the Drawdown Reduction Manager involves risks, including the potential loss of capital. You agree to use this application at your own risk and understand that the developer of the application (the author) is not liable for any losses incurred.

3. **Not Responsible for Trading Results**: The Drawdown Reduction Manager is a tool for trade synchronization and drawdown reduction, but it does not guarantee profitable trades or specific results. The author is not responsible for any trading outcomes, including financial losses or missed trading opportunities.

4. **Personal Responsibility**: You are solely responsible for your trading decisions and the execution of trades. The author of the Drawdown Reduction Manager is not responsible for any trading actions taken by you or any consequences that may arise from those actions.

5. **Review and Validate**: Before using the Drawdown Reduction Manager with live trading accounts or real money, thoroughly review and validate its functionality in a simulated or demo environment. Understand the risks involved and ensure compatibility with your specific trading setup.

6. **No Liability**: The author of the Drawdown Reduction Manager disclaims all liability for any direct, indirect, incidental, special, consequential, or exemplary damages resulting from the use or inability to use the application.# Drawdown-Reduction
