# test_data.py
BASE_URL = "https://stellarburgers.nomoreparties.site"
INGREDIENTS_URL = f"{BASE_URL}/api/ingredients"
REGISTER_URL = f"{BASE_URL}/api/auth/register"
LOGIN_URL = f"{BASE_URL}/api/auth/login"
LOGOUT_URL = f"{BASE_URL}/api/auth/logout"
REFRESH_TOKEN_URL = f"{BASE_URL}/api/auth/token"
USER_URL =  f"{BASE_URL}/api/auth/user"
ORDER_URL = f"{BASE_URL}/api/orders"


VALID_USER = {
    "email": "test-user@example.com",
    "password": "testpassword",
    "name": "Test User"
}

EXISTING_USER = {
    "email": "existing-user@example.com",
    "password": "existingpassword",
    "name": "Existing User"
}

INVALID_USER = {
    "email": "invalid-user@example.com",
    "password": "invalidpassword"
}

UPDATED_USER = {
    "email": "updated_user_@example.com",
    "password": "newpassword123",
    "name": "UpdatedUser"
}