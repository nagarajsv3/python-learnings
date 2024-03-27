dictionary = {
    "Jan": "January",
    "Feb": "Febraury",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(dictionary)
print(dictionary["Jan"])
print(dictionary.get("Mar"))
print(dictionary.get("Cla", "Invalid Key"))

dictionary = {
    1: "January",
    2: "Febraury",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

print(dictionary)
print(dictionary[2])
print(dictionary.get(3))
print(dictionary.get(14, "Invalid Key"))