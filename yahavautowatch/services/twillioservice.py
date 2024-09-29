from twilio.rest import Client

def send_order_whatsapp_message(name, quantity, order_number):
    # Twilio credentials from the Twilio console
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    twilio_number = 'whatsapp:+14155238886'  # Example WhatsApp-enabled Twilio number

    # Initialize the Twilio client
    client = Client(account_sid, auth_token)

    # Message template
    message_body = f"Hello , i need to  order of {name} in this quantity {quantity}  . 
    thank you so much 
    order number {order_number}."

    # Send the message
    message = client.messages.create(
        body=message_body,
        from_=twilio_number,
        to='whatsapp:your_personal_whatsapp_number'  # Replace with recipient's number
    )

    print(f"Message sent! SID: {message.sid}")

# Example usage

def send_first_customer_whatsapp_message(name, quantity, order_number,watchname):
    # Twilio credentials from the Twilio console
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    twilio_number = 'whatsapp:+14155238886'  # Example WhatsApp-enabled Twilio number

    # Initialize the Twilio client
    client = Client(account_sid, auth_token)

    # Message template
    message_body = f"Hello {name}, your order of {watchname}  has been processed. Your order number is {order_number}.
    Thank you very much and we will be in touch"

    # Send the message
    message = client.messages.create(
        body=message_body,
        from_=twilio_number,
        to='whatsapp:your_personal_whatsapp_number'  # Replace with recipient's number
    )

    print(f"Message sent! SID: {message.sid}")


def send_shipping_customer_whatsapp_message(name ,tracking_number,watchname):
    # Twilio credentials from the Twilio console
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    twilio_number = 'whatsapp:+14155238886'  # Example WhatsApp-enabled Twilio number

    # Initialize the Twilio client
    client = Client(account_sid, auth_token)

    # Message template
    message_body = f"Hello {name}, your order of {watchname}  has been shipped. Your order number is {tracking_number}.
    Thank you very much and we will be in touch"

    # Send the message
    message = client.messages.create(
        body=message_body,
        from_=twilio_number,
        to='whatsapp:your_personal_whatsapp_number'  # Replace with recipient's number
    )

    print(f"Message sent! SID: {message.sid}")

def send_arrived_customer_whatsapp_message(name ,tracking_number,watchname):
    # Twilio credentials from the Twilio console
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    twilio_number = 'whatsapp:+14155238886'  # Example WhatsApp-enabled Twilio number

    # Initialize the Twilio client
    client = Client(account_sid, auth_token)

    # Message template
    message_body = f"Hello {name},  We saw that the order of {watchname}  has been deliverd .
    We will be happy to hear about your experience"

    # Send the message
    message = client.messages.create(
        body=message_body,
        from_=twilio_number,
        to='whatsapp:your_personal_whatsapp_number'  # Replace with recipient's number
    )

    print(f"Message sent! SID: {message.sid}")
