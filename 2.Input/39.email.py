# ----------------------------------------------------
#! print email username and website
# ----------------------------------------------------
name = input("what's your name: ").strip().capitalize()
email = input("what's your email: ").strip().lower()

theUsername = email[: email.index("@")]
theWebsite = email[email.index("@") + 1 :]

print(f"Hello {name} Your email is {email}")
print(f"Your username is {theUsername} & your website is {theWebsite}")
# ----------------------------------------------------
