def selection_sort(nums):  # Seleciton_sort function is initialized

    arr = nums.copy()
    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i+1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        y = arr[min_index]  # y stores the value of the min_index

        arr[min_index] = arr[i]

        arr[i] = y  # lower number and other number replace

    return arr


def extract_temps(temps):  # extract_temps is initalized

    temp_list = []
    n = len(temps)

    for i in range(n):

        # Try and except converts temp values to a float
        # Unconvertable strings are passed through an excepetion

        try:
            temp_float = float(temps[i])
            temp_list.append(temp_float)

        except:
            pass

    return temp_list


def calculate_median(temps):  # Calculate_median function is initialized

    temp_list = extract_temps(temps)

    length_temp_list = len(temp_list)

    # Checks if list contains odd/even number of items
    even_odd_check = length_temp_list % 2

    z = int(length_temp_list/2)

    if even_odd_check == 0:  # Even
        median = ((temp_list[z-1]) + (temp_list[z]))/2  # Median calculaton
    else:  # Odd
        median = temp_list[z]

    return median


def main(temps):  # Main function is initialized

    try:

        temp_list = extract_temps(temps)  # temp values are extracted

        ordered_list = selection_sort(temp_list)  # temp values are re-ordered

        # median of temp values is determined
        median = calculate_median(ordered_list)

        return median

    except:

        return 'N/A'  # retuns N/A if no items are convertable to strings


temps = ["5", "", "5.5", "6.2", "4.5", "N/A", "Not Recorded", "5.67"]
print("Given Temps:", temps)
print("Median:", main(temps))
