# StudentCouncilBot
Bot for student council of SPb

# Prerequisites

1. [Python](https://python.org/) version 3.8 or later
2. pip or pip3
3. Bot token for VK API
4. Google App Password [Guide](https://support.google.com/accounts/answer/185833?hl=en#:~:text=Create%20%26%20use%20App%20Passwords)

# Instructions
## Installing requirements
1. Clone this repo 

    ```shell
    git clone https://github.com/kill-your-soul/StudentCouncilBot.git
    ```
2. Create virtual environment 
    
    - For Windows:

        ```Powershell
        python -m venv .venv
        ```

    - For Linux, MacOS:
    
        ```shell
        python3 -m venv .venv
        ```

3. Activate virtual environment

    - For Windows:
    
        ```Powershell
        .\.venv\Scripts\activate
        ```

    - For Linux, MacOS:

        ```shell
        source ./.venv/bin/activate
        ```

4. Install requirements

    - For Windows:

        ```shell
        pip install -r requirements.txt
        ```

    - For Linux, MacOS:
    
        ```shell
        pip3 install -r requirements.txt
        ```

1. Setting environment variables

    - For Windows:

        + Powershell:

            ```Powershell
            $env:TOKEN = "TOKEN_TO_YOUR_BOT";
            $env:GOOGLE_APP_PASSWORD = "YOUR_GOOGLE_APP_PASSWORD";
            ```
        
        + cmd:

            ```cmd
            set TOKEN=TOKEN_TO_YOUR_BOT
            set GOOGLE_APP_PASSWORD=YOUR_GOOGLE_APP_PASSWORD
            ```

    - For Linux, MacOS:

        + Bash:

            ```shell
            export TOKEN="TOKEN_TO_YOUR_BOT"
            export GOOGLE_APP_PASSWORD="YOUR_GOOGLE_APP_PASSWORD"
            ```