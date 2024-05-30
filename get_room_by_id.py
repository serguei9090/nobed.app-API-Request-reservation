import cloudscraper


def get_room_name(room_id=2376063):
    """Fetches the room name ("title") for a given room ID from the nobeds.com API.

    Args:
        id (int, optional): The room ID to retrieve the name for. Defaults to 2376063.

    Returns:
        str: The room title ("Full House") if successful, otherwise None.
    """

    # Create a cloudscraper instance
    scraper = cloudscraper.create_scraper()

    # Construct the URL with API key (replace with your actual key)
    url = "https://api.nobeds.com/api/Rentals/jVkw6rmAHblkwaqtued0/"

    # Make the request using the scraper
    response = scraper.get(url, headers={"accept": "application/json"})

    # Check for successful response
    if response.status_code == 200:
        # Parse the JSON response
        room_data = response.json()
        for room in room_data:
            rooms_id = room.get("room_id")
            title = room.get("title")
            if rooms_id == room_id:
                return title

# Handle cases where no match is found
    else:
        print(f"Error: Request failed with status code {response.status_code}")
        return None  # Return None on error



# Example usage with default room ID (2376063)
# room_title = get_room_name(2376067)
# if room_title:
#     print(room_title)  # Print the retrieved room title
# else:
#     print("Room title not found or API error occurred.")