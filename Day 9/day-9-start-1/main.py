#Nesting
capitals = {
    "France": "Paris",
    "Tanzania": "Arusha",
    "Uganda": "Kampala",
    "Sudan": "Khartoum"
}

# Nesting a list in a dictionary
# Below the key is a string and the value is a list
travel_log = {
    # Nesting a dictionary in a dictionary
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 14
    },
    # Nesting a dictionary in a list
    "Kenya": {
        "cities_visited": ["Nairobi", "Naivasha", "Meru"],
        "people_seen": {["Esther", "John", "Sally"]}
    },
}

travel_log = [
    # Nesting a dictionary in a list, the dictionary has 3 key value pairs
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 14
    },
    {
        "country": "Kenya",
        "cities_visited": ["Nairobi", "Naivasha", "Meru"],
        "people_seen": {["Esther", "John", "Sally"]}
    },
]

print(travel_log)
