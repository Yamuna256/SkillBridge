for attempt in range(2):  # Allow 2 attempts in total
    # Get user input
    username = input("Enter your username: ").strip().upper()  # Normalize username
    password = input("Enter your password: ")

    # Basic validation for empty input
    if not username or not password:
        print("Username and password cannot be empty. Please try again.")
        continue

    # Check if the credentials are correct
    if username == correct_username and password == correct_password:
        print("Sign-in successful!")
        send_successful_sign_in_sms()  # Call function to send SMS
        return  # Exit the function on successful sign-in
    else:
        if attempt < 1:  # If not the last attempt
            print("Invalid username or password. Please try again.")
        else:
            print("Invalid username or password. No attempts remaining.")
print("Sign-In failed please contact customer support!")