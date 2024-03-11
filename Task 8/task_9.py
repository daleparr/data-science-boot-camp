# Email class definition
class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True

# List to store Email objects
inbox = []

# Function to populate the inbox with sample emails
def populate_inbox():
    sample_emails = [
        Email("sender1@example.com", "Welcome to HyperionDev!", "Content of email 1."),
        Email("sender2@example.com", "Great work on the bootcamp!", "Content of email 2."),
        Email("sender3@example.com", "Your excellent marks!", "Content of email 3.")
    ]
    inbox.extend(sample_emails)

# Function to list all emails with their indices
def list_emails():
    for index, email in enumerate(inbox):
        print(f"{index} {email.subject_line} {'(Read)' if email.has_been_read else ''}")

# Function to read a specific email by index
def read_email(index):
    email = inbox[index]
    email.mark_as_read()
    print(f"\nEmail from {email.email_address}:\nSubject: {email.subject_line}\nContent: {email.email_content}\n")

# Populate inbox with sample emails at startup
populate_inbox()

# Main program loop
while True:
    print("\n1. Read an email\n2. View unread emails\n3. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        list_emails()
        email_index = int(input("Enter the email index to read: "))
        read_email(email_index)
    elif choice == "2":
        for email in inbox:
            if not email.has_been_read:
                print(f"{email.subject_line} - Unread")
    elif choice == "3":
        break
    else:
        print("Invalid option. Please try again.")
