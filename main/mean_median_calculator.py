"""
Python code to calculate median and mode from a given list.
"""


def calculate_median(price_list):
    """
    Function to calculate median from a given list.
    :param price_list:
    :return median:

    Steps to find a median:
    1. Sort the given values in ascending order
    2. Evaluate whether number of elements in the list are odd or even
       For even number of elements calculate the average of middle two numbers
       For odd number of elements pick the middle element by dividing the length by 2
    """

    price_list_sorted = sorted(price_list)
    print(price_list_sorted)
    price_list_len = len(price_list_sorted)

    if price_list_len % 2 == 0:  # List contains even number of elements
        mid_idx = int(price_list_len / 2)
        median = int((price_list_sorted[mid_idx - 1] + price_list_sorted[mid_idx]) / 2)
    else:  # List contains odd number of elements
        mid_idx = int(price_list_len / 2)
        median = int((price_list_sorted[mid_idx]))

    return median


def calculate_mode(sales):
    """
    Function to calculate mode from a given list.
    :param sales:
    :return mode_value:

    Steps to find a mode:
    1. Sort the given values in ascending order
    2. Compare two consecutive elements and increment the current_count when they are same.
    3. Compare max_count with current_count
       When the current_count is greater than max_count then update it to latest current_count
    """

    sales_sorted = sorted(sales)
    print(sales_sorted)

    max_count = 1
    current_count = 1
    mode_value = sales_sorted[0]
    for i in range(len(sales_sorted) - 1):
        if sales_sorted[i] == sales_sorted[i + 1]:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
                mode_value = sales_sorted[i + 1]
        else:  # Reset the count when the element is different
            current_count = 1

    return mode_value


if __name__ == '__main__':
    price_lst = [12, 11, 9, 12, 88, 111, 86, 103, 87, 95, 78, 77, 85, 86, 12, 111, 10, 111, 95, 6, 95]
    median = calculate_median(price_lst)
    print("Median of the above list = {}".format(median))

    sales_qty = [19, 86, 87, 88, 111, 95, 86, 103, 9, 87, 95, 78, 77, 85, 86, 12, 11, 10, 111, 6, 95, 95]
    mode = calculate_mode(sales_qty)
    print("Mode of the above list = {}".format(mode))
