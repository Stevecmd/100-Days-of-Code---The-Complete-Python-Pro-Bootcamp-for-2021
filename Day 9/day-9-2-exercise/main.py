travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇


def add_new_country(country_visited, new_visits, new_cities):
    new_country = {}
    # Method 1 assign them individually
    # new_country["country"] = country_visited,
    # new_country["visits"] = new_visits,
    # new_country["cities"] = new_cities

    # Method 2 - assign them as a list
    new_country["country", "visits",
                "cities"] = country_visited, new_visits, new_cities
    travel_log.append(new_country)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
