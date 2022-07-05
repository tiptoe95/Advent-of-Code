#!/bin/python3


#


def count_increases(arr):
    increases = 0
    for i, depth in enumerate(arr):
        try:
            if arr[i+1] > depth:
                increases += 1
        except IndexError:
            continue
    return increases


def average(arr):
    return sum(arr) / len(arr)


def reduce_noise(signal):
    clean_signal = []
    for i in range(len(signal)-2):
        clean_signal.append(average(signal[i:i+3]))
    return clean_signal


def sum_windows(signal):
    sums = []
    for i in range(len(signal)-2):
        sums.append(sum(signal[i:i+3]))
    return sums


def get_input():
    input_path = r"input_day1.txt"
    with open(input_path, 'r') as input_file:
        lst = [int(x) for x in input_file.readlines()]
    return lst


def main():
    floor_chart = get_input()
    increases = count_increases(floor_chart)
    sums = sum_windows(floor_chart)
    sum_increases = count_increases(sums)
    print(sum_increases)


def test():
    floor_chart = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    increases = count_increases(floor_chart)
    sums = sum_windows(floor_chart)
    print(sums)
    print(count_increases(sums))


if __name__ == "__main__":
    #test()
    main()
