# Telegram Messages Cleaner Script

## Overview

This Python script uses the Telethon library to connect to your Telegram account and delete all messages from all your conversations. Please note that this action is irreversible, and all messages in your chats will be permanently deleted.

## Prerequisites

Before running the script, make sure you have the following:

1. Telegram API credentials (API ID and API hash). You can obtain them by creating a new application on the [Telegram website](https://my.telegram.org/auth).
2. Python installed on your machine.

## Usage

1. Clone this repository to your local machine.

    ```bash
    git clone https://github.com/sahiljani/telegram-messages-cleaner.git
    ```

2. Install the required Python packages.

    ```bash
    pip install telethon
    ```

3. Run the script.

    ```bash
    python delete_messages.py
    ```

4. Enter your Telegram API credentials (API ID and API hash) and your phone number when prompted.

5. The script will connect to your Telegram account and delete all messages in your conversations.

## Important Notes

- Use this script at your own risk. Deleting messages is irreversible, and there is no way to recover them.
- Ensure you have a backup of any important information before running the script.

## Contribution

Feel free to contribute to this project by opening issues or creating pull requests. Any suggestions or improvements are welcome!
