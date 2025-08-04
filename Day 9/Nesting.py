# {
#     Key: [List],
#     key2: {Dict}
# }


capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    
}

# Nested list in dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}


nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])




travel_log = {
    "France": {
        "num_times_visited" : 8,
        "cities_visits" : ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "num_times_visited" : 3,
        "cities_visits" : ["Stuttgart", "Berlin"]
    }
}

print(travel_log["France"])