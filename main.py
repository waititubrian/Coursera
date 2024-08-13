def record_profit_years(recent_first, recent_last):
    recent_first = [2022, 2018, 2011, 2006]
    recent_last = [1989, 1992, 1997, 2001]

    # Reverse the order of the "recent_first" list so that it is in
    # chronological order.
    recent_first.reverse()

    # Extend the "recent_last" list by appending the newly reversed
    # "recent_first" list.
    recent_last.extend(recent_first)

    # Return the "recent_last", which now contains the two lists
    # combined in chronological order.
    return recent_last

# Call the record_profit_years() function with default empty lists.
print(record_profit_years([], []))\

//////////////////