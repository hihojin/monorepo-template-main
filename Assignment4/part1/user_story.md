As a new customer of Paypal I can sign up/register as a new user, so that I can create my account.

Acceptance Criteria:

1. email field is required. If this field is empty or not a valid email we need to show an error message.
2. If email is valid, we need to verify if this is an existing user or not. If exist, redirect to login page. If it is a new user, continue to the next page.
3. Phone number is required. If this is empty, shows a message to user. If a number is not valid, shows the message. If number is valid, continue to the next page.
4. user receives a security code within 1 minute after clicking next button in phone number page. If user not receives the message user can re-enter phone number. 
5. The security code should expire in 10 minutes and not available after 10 minutes. 
