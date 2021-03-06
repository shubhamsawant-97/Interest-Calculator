# monthly
def monthly(amount, rate_of_interest, period):
    # print(f"Amount = {amount}")
    # print(f"rate of interest = {rate_of_interest}")
    # print(f"period = {period}")
    roi = amount * rate_of_interest / 100
    monthly_interest = roi / 12
    return f"Your monthly interest will be {monthly_interest} Rupees Only"


# quaterly
def quarterly(amount, rate_of_interest, period):
    if period % 3 == 0:
        yearly_int = (amount * rate_of_interest) / 100
        quarterly_int = yearly_int / 4
        return quarterly_int
    else:
        yearly_int = (amount * rate_of_interest) / 100
        quarters = period // 3
        print(f"There are {quarters} quarters")
        remaining_months = period % 3
        print(f"There are {remaining_months} remaining months")
        quarterly_int = yearly_int / 4
        int_of_rem_months = (yearly_int / 12) * remaining_months
        return f"quartetly interest is {quarterly_int} and interest for last {remaining_months} is {int_of_rem_months}"




# half yearly
def half_yearly(amount, rate_of_interest, period):
    if period % 6 == 0:
        yearly_int = (amount * rate_of_interest) / 100
        half_int = yearly_int / 2
        return f"Half yearly interest is{half_int}"
    else:
        yearly_int = (amount * rate_of_interest) / 100
        semisters = period // 6
        print(f"There are {semisters} semisters")
        remaining_months = period % 6
        print(f"Remaining months are {remaining_months}")
        half_yearly_interest = yearly_int / 2
        int_of_rem_months = (yearly_int / 12) * remaining_months
        return f"Half yearly interest is {half_yearly_interest} and interest for remaining months is {int_of_rem_months}"




# yearly interest
def yearly(amount, rate_of_interest, period):
    if period % 12 == 0:
        yearly_int = (amount * rate_of_interest) / 100
        return f"Interest per annum is {yearly_int}"
    else:
        yearly_int = (amount * rate_of_interest) / 100
        rem_months = period % 12
        int_of_rem_months = (yearly_int / 12) * rem_months
        return f"Interest per annum is {yearly_int} and interest for remaining {rem_months} months is {int_of_rem_months}"


