# Streamlit Google OAuth Demo

## Setup
Directory structure should look like this
```
├── app.py
├── auth/
│   ├── __init__.py
│   ├── authenticate.py
│   └── token_manager.py
│── .env
└── client_secret.json
```
The `.env` file should have these values
```
TOKEN_KEY=your_jwt_key_here
ALLOWED_USERS=user1@gmail.com,user2@gmail.com
```
`client_secret.json` can be downloaded from google cloud console. 

## Demo
Login and Logout

![login_and_logout](https://github.com/user-attachments/assets/80864479-f463-4a2e-b5ea-623630967435)

If a user without permission logs in, they will get a access denied message

![access_denied](https://github.com/user-attachments/assets/12e1721f-f4af-4c08-8f74-7fd85339d3e1)

If the jwt expired, the user will be unable to login and gets a token expired message

![jwt_expired](https://github.com/user-attachments/assets/dc3f746a-d5bf-4b74-bac3-08ca2634a36e)

