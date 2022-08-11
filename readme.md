# StudentCouncilBot
Bot for student council of SPb

# Prerequisites

1. [Python](https://python.org/) version 3.8 or later
2. pip or pip3
3. Bot [token](https://dev.vk.com/api/bots/getting-started#%D0%9F%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BA%D0%BB%D1%8E%D1%87%D0%B0%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%B0) for VK API
4. Google App Password [Guide](https://support.google.com/accounts/answer/185833?hl=en#:~:text=Create%20%26%20use%20App%20Passwords)
5. You need Excel table(.xlsx) in `static` directory

# Image from Docker Hub
```shell
docker run --env TOKEN='TOKEN_TO_YOUR_BOT' `
--env GOOGLE_APP_PASSWORD='YOUR_GOOGLE_APP_PASSWORD'
--name name_of_your_container -d killyoursoul/student_council_bot
```
# Image from source
1. Clone this repo

    ```shell
    git clone https://github.com/kill-your-soul/StudentCouncilBot.git
    ```
2. Build image 

    ```shell
    docker build -t name_of_your_image .
    ```

3. Run container 

    ```shell
    docker run --env TOKEN='TOKEN_TO_YOUR_BOT' `
    --env GOOGLE_APP_PASSWORD='YOUR_GOOGLE_APP_PASSWORD' `
    --name name_of_your_container -d name_of_your_image
    ```


# Build locally
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