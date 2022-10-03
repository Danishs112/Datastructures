# collect email from user
# split the email using the @, first part as the username, the second part is gonna
# saved as domain

# split domain using .
def email_slicer():

    while True:
        email = input("Enter the email address: ")
        username, domain = email.split("@")
        domain_address, domain_type = domain.split('.')
        print("User Name: " + username)
        print("Domain Address: " + domain_address)
        print("Domain Type: " + domain_type)


email_slicer()
