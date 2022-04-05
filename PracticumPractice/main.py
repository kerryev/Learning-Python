from Guest_class import Guest
textfile = open('guest_list.txt')

# ------------------------------------------------------------------------------


def park_expenses(num_employees, wage, num_rides):

    expenses = (num_employees * wage * 8) + (num_rides * 10000)
    return expenses


def revenue_and_profit(expenses, gross_margin_percent):
    x = []

    required_revenue = expenses/(1 - gross_margin_percent)
    gross_profit = required_revenue - expenses

    x.append(required_revenue)
    x.append(gross_profit)

    return x


def create_guests(guest_attributes):

    new_guest = Guest(guest_attributes[0], guest_attributes[1])
    new_guest.set_stamina(guest_attributes[2])
    new_guest.set_hunger(guest_attributes[3])
    new_guest.set_money_spent()

    return new_guest

# ---------------------------------------------------------------------------------


def main():

    start_up = 1000000
    num_rides = 15
    num_employees = 250
    wage = 25
    gross_margin_profit = 0.20

    expenses = round(park_expenses(num_employees, wage, num_rides), 2)

    revenue_profit = revenue_and_profit(expenses, gross_margin_profit)

    days = 0
    y = True
    total_gross_profit = 0

    print('Gross Profit' + '   ' + 'Day #')

    while y == True:

        total_gross_profit += revenue_profit[1]

        if total_gross_profit > start_up:
            y = False

        else:
            days += 1
            print(str(round(total_gross_profit, 2)) + '      ' + str(days))

    # ---------------------------

    for i in textfile:
        split_str = i.split()
        split_str[0] = str(split_str[0])
        split_str[1] = int(split_str[1])
        split_str[2] = int(split_str[2])
        split_str[3] = int(split_str[3])

        new_guest = create_guests(split_str)
        print(new_guest.get_name() + ' will spend ' +
              str(round(new_guest.get_money_spent(), 2)) + ' at the park')


main()
