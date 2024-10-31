birthdays = {
    "Jabir": "2004-08-28",
    "Zakir": "1989-11-08",
    "Zainab": "2000-11-08",
    "Papa": "1965-07-05"
}

# Function to search and format birthday
def find_birthday(name):
    # Check if the name is in the dictionary
    if name in birthdays:
        # Use split to break the date into components
        date_parts = birthdays[name].split("-")
        
        # Join the date parts in a new format
        formatted_birthday = "/".join(date_parts[::-1])  # Format as DD/MM/YYYY
        return f"{name}'s birthday is on {formatted_birthday}."
    else:
        return f"No birthday found for {name}."

# Example usage
name_to_search = "Jabir"
result = find_birthday(name_to_search)
print(result)
