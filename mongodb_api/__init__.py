import os


if __name__ == '__main__':

    os.system('uvicorn mongodb_api.api:app --reload --port 8000') # Run the API
