def how_much_coffee(events):

    coffee_count = 0
    for event in events:
        if event != event.lower():
            coffee_count += 2
        else:
            coffee_count += 1
    return coffee_count
    return coffee_count

    # if "cw" or "cat" or "dog" or "movie":
    #     return 1
    # elif "dog" and "cat":
    #     return 2

    # elif "CW" or "CAT" or "DOG" or "MOVIE":
    #     return 2

    # else:
    #     return 0

