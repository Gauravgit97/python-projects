import pyshorteners

url = input("Enter the URL here:\n")

print("The shorted URL:\n ",pyshorteners.Shortener().tinyurl.short(url))