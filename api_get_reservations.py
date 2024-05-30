#!/usr/bin/env python
#import requests
import cloudscraper
#import json

from datetime import date
from inputdate import calculate_future_date
from get_room_by_id import get_room_name
from create_table import table
from mail_send import send_email
# Create a cloudscraper instance
scraper = cloudscraper.create_scraper()

fromdate = str(date.today())
# fromdate = "2024-04-30"
todate = str(calculate_future_date())
# todate = "2024-06-1"
#Api_token
api_token = "apitoken"
# Construct the URL with query parameters
url = "https://api.nobeds.com/api/Bookings/"+api_token+"?fromdate=" + fromdate +"&todate=" + todate

# Make the request using the scraper
response = scraper.get(url, headers={"accept": "application/json"})

# Check for successful response (optional)
if response.status_code == 200:
    #print(response.text)
    # Parse the JSON response
    data = response.json()
    
else:
    print(f"Error: Request failed with status code {response.status_code}")

# Create an empty list to store the extracted information
booking_info = []

# Iterate through each booking object
for booking in data:
# Extract desired information
    name = booking.get("name")
    checkin = booking.get("checkin")
    checkout = booking.get("checkout")
    email = booking.get("email")
    phone = booking.get("phone")
    guests = booking.get("guests")
    children = booking.get("childrens")  # Corrected typo (childrens)
    nights = booking.get("nights")
    services = booking.get("services")
    price = booking.get("price")
    total = booking.get("total")
    comment = booking.get("comment")
    referral = booking.get("referral")
    country = booking.get("country")
    status = booking.get("status")
    #roomid= booking.get("room_id")
    room = get_room_name(booking.get("room_id"))


# Create a dictionary for each booking with extracted data
    booking_details = {
        "Room": room,
        "checkin": checkin,
        "checkout": checkout,
        "nights": nights,
        "name": name,
        "guests": guests,
        "children": children,
        "email": email,
        "phone": phone,
        "country": country,
        "status": status,
        "referral": referral,
        "services": services,
        "price": price,
        "total": total,
        "comment": comment,
        
        
        
        
    }

# Append the booking details dictionary to the list
    booking_info.append(booking_details)

#print(df.to_html())
# print(json.dumps(booking_info, indent=4))
# Apply styles using Styler object
booking_body=table(booking_info)
send_email(booking_body)
# with open('bookings.html', 'w') as f:
#     f.write(booking_body)