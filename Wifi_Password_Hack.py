# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 23:22:28 2023

@author: KIIT
"""

import subprocess

def get_wifi_password():
    # Run the netsh command to get the Wi-Fi profile information
    command = 'netsh wlan show profile name="Now You See Me_5G" key=clear'
    output = subprocess.check_output(command, shell=True).decode('utf-8')

    # Search for the Key Content field in the output
    keyword = "Key Content"
    start_index = output.index(keyword) + len(keyword) + 2
    end_index = output.index('\r', start_index)
    password = output[start_index:end_index]

    return password

# Call the function to retrieve the Wi-Fi password
wifi_password = get_wifi_password()
print("Wi-Fi Password:", wifi_password)
