def clock():            # This code converts the seconds entered into a more meaningful
                        # clock equivalent. It helps users determine the
                        # amount of hours, minutes and seconds for any given figure.
                        # FUTURE UPDATE SHOULD HAVE A DAYS ENTRY!!!

    seconds_per_minute = 60
    seconds_per_hour = 60*seconds_per_minute
# Next assign necessary variables to seconds, minutes and hours

# For seconds,
    seconds = eval(input("enter seconds to convert: \n"))


# Next for hours. cal the number of seconds in an hour followed by the number of seconds remaining
    hours = seconds//seconds_per_hour
    seconds %= seconds_per_hour

# Next for minutes. cal the number of seconds in one minute followed by the number of minutes remaining
    minutes = seconds//seconds_per_minute
    seconds %= seconds_per_minute

    if hours > 0:
        if hours == 1:
            print(hours, "hour", end=" ")

        else:
            print(hours, "hours", end=" ")

    if minutes > 0:
        if minutes == 1:
            print(minutes, "minute", end=" ")
        else:
            print(minutes, "minutes", end=" ")

    if seconds > 0:
        if seconds == 1:
            print(seconds, "second", end=" ")
        else:
            print(seconds, "seconds")

clock()

while True:
    clock()

    ''' to quit this program, press the letter
    or press enter key to continue
    '''

    quits = input("Press 'E' to exit or press 'enter' to continue: \n")
    if quits:
        if quits == "E" or quits == "e":
            break
        else:
            continue
