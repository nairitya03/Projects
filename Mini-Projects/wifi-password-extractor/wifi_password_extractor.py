import subprocess as sb
import time

# Get a list of Wi-Fi profiles
profiles = sb.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split("\n")
profiles = [i.split(":")[1][1:-1] for i in profiles if "All User Profile" in i]

# Iterate over each profile and extract the password
for profile in profiles:
    results = sb.check_output(['netsh', 'wlan', 'show', 'profiles', profile, 'key=clear']).decode('utf-8').split("\n")
    password = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    
    # Handle cases where no password is found
    if password:
        print("{:<30}| {:<}".format(profile, password[0]))
    else:
        print("{:<30}| {:<}".format(profile, ""))
    
# Wait for 15 seconds
time.sleep(15)
