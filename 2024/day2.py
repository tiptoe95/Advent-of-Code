#!/usr/bin/python3


#


def main():
    input_path = r'inputs/day2.txt'
    reports = get_input(input_path)
    for report in reports:
        rep = Report(report)
    # Part 1
    part1()
    # Part 2
    part2()
    return


class Report():
    census = []
    unsafe_reports = []
    tolerable_reports = []

    def __init__(self, readings: list[int], temp=False):
        if not temp:
            Report.census.append(self)
            self.idx = len(Report.census)
        self.readings = readings
        self.length = len(readings)
        self.deltas = self.get_deltas()
        self.is_safe = None
        self.fail_reason = None
        self.check_safety(temp)
        return

    def __str__(self):
        str1 = f"report{self.idx}: {self.readings}"
        str2 = f"deltas: {self.deltas}"
        str3 = f"status: {self.safety_status()}"
        if not self.is_safe:
            str3 += f" - {self.fail_reason}"
        return '\n'.join((str1, str2, str3, ""))

    def get_deltas(self) -> list[int]:
        deltas = [ self.readings[i+1] - self.readings[i] for i in range(self.length - 1)]
        return deltas

    def check_safety(self, temp=False):
        if not self.check_rate():
            self.fail_reason = "rate"
            self.is_safe = False
            if not temp:
                Report.unsafe_reports.append(self)
            return
        if not self.check_inflection():
            self.fail_reason = "inflection point"
            self.is_safe = False
            if not temp:
                Report.unsafe_reports.append(self)
            return
        self.is_safe = True

    def check_rate(self) -> bool:
        if all([1 <= x <= 3 for x in map(abs, self.deltas)]):
            return True
        return False

    def check_inflection(self) -> bool:
        signs_pos = [x>0 for x in self.deltas]
        signs_neg = [x<0 for x in self.deltas]
        if all(signs_pos) or all(signs_neg):
            return True
        return False

    def safety_status(self) -> str:
        match self.is_safe:
            case None:
                return "status unknown"
            case True:
                return "safe"
            case False:
                return "not safe"
        return "ERROR"

    @classmethod
    def find_tolerables(cls):
        for report in cls.unsafe_reports:
            if report.check_tolerance():
                cls.tolerable_reports.append(report)
        return

    def check_tolerance(self) -> bool:
        '''returns true if the report is tolerable'''
        for i in range(self.length):
            temp_report_readings = [x for x in self.readings]
            del temp_report_readings[i]
            temp_report = Report(temp_report_readings, temp=True)
            if temp_report.is_safe:
                return True
        return False


def part1():
    count = 0
    for report in Report.census:
        if not report.is_safe:
            print(report)
        else:
            count += 1
    print(f"Part 1: {count} safe reports")
    return


def part2():
    Report.find_tolerables()
    safe_count = len(Report.census) - len(Report.unsafe_reports)
    new_safe_count = safe_count + len(Report.tolerable_reports)
    print(f"Part 2: {new_safe_count} tolerable reports")
    return


def get_input(filepath):
    with open(filepath, 'r') as file:
        data = [ [int(value) for value in line.strip().split()]
                for line in file.readlines()]
    return data


def test():
    reports = [
        [7,6,4,2,1],
        [1,2,7,8,9],
        [9,7,6,2,1],
        [1,3,2,4,5],
        [1,3,6,7,9]]
    part1(reports)


if __name__ == '__main__':
    main()
