#!/usr/bin/python3


#


def main():
    input_path = r'inputs/input_day6.txt'
    buffer = get_data(input_path)
    
    # Part 1
    first_signal_idx = start_of_packet(buffer)
    print(f"Part 1:\n{first_signal_idx}")

    # Part 2
    message_idx = start_of_message(buffer)
    print(f"Part 2:\n{message_idx}")


def get_data(path: str) -> str:
    with open(path, 'r') as file:
        data = file.read()
        data = data.rstrip()
    return data


def start_of_packet(buffer: str) -> int:
    for i in range(len(buffer) - 3):
        signal = buffer[i:i+4]
        if len(set(signal)) == 4:
            return i+4
    return None


def start_of_message(buffer: str) -> int:
    for i in range(len(buffer) - 13):
        signal = buffer[i:i+14]
        if len(set(signal)) == 14:
            return i+14
    return None


def test():
    buffer1 = ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7, 19)
    buffer2 = ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5, 23)
    buffer3 = ("nppdvjthqldpwncqszvftbrmjlhg", 6, 23)
    buffer4 = ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10, 29)
    buffer5 = ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11, 26)

    test1 = [buffer1, buffer2, buffer3, buffer4, buffer5]
    for i, test in enumerate(test1):
        result = start_of_packet(test[0])
        print(f"test {i} of {len(test1)}: {result}")
        if result != test[1]:
            print(f"\tresult was {result}, should be {test[1]}")
        
    for i, test in enumerate(test1):
        result = start_of_message(test[0])
        print(f"test {i} of {len(test1)}: {result}")
        if result != test[2]:
            print(f"\tresult was {result}, should be {test[2]}")


if __name__ == "__main__":
    main()
