# zimp-orchestrator
A simple python service which handles reproducible zimp experiments


## MLFlow Set-Up
Uses information from https://towardsdatascience.com/deploy-mlflow-with-docker-compose-8059f16b6039  
Steps:  
1. Create an `.env` file with required variables (Run the command below if you are unsure which are required) - In a demo-setting the values can be chosen arbitrarily
2. Run `docker-compose up -d --build`
3. Wait for completion and then check `127.0.0.1:80`
