"""
Proprietary License

Copyright 2024 Bueezi™
All Rights Reserved.

This software is licensed under the Proprietary License. Unauthorized copying, modification, distribution, or use
of this software is strictly prohibited. For full license details, see the LICENSE file in this repository.
"""

current_cookie=0
cookies = None
uses = 0
with open("cookies.txt", "r") as f:
    cookies = [_.replace("\n", "") for _ in f.readlines()]
cookie = cookies[0]

def Get_Cookie():
    global uses, cookie, current_cookie
    uses+=1
    if uses>2000:
        print(f"COOKIE SWAPPING WE NOW ON COOKIE : {current_cookie}")
        current_cookie = current_cookie + 1 if current_cookie < len(cookies)-1 else 0
        cookie = cookies[current_cookie]
        uses = 0
    return cookie