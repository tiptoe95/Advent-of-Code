from pathlib import Path


def flatten(ls, flattened_list=[]):
    for element in ls:
        if type(element) != list:
            flattened_list.append(element)
        else:
            flatten(element, flattened_list)
    return flattened_list


def overlap(canvas, claims):
    for i, claim in enumerate(claims):
        claim = claim.replace('@', '').replace(':', '').replace('x', ',').split()
        claims[i] = claim[1:]
    for c, claim in enumerate(claims):
        for i, coord in enumerate(claim):
            claims[c][i] = coord.split(',')
    for claim in claims:
        claim_start, claim_dim = claim
        x, y = claim_start
        length, height = claim_dim
        x, y, length, height = map(int, [x, y, length, height])
        for i in range(height):
            for z, val in enumerate(canvas[y + i][x:x + length]):
                canvas[y+i][x+z] = val + 1
    return canvas, claims


def find_claim(canvas1, claims):
    unconflicted_claim = 0
    # get the overlap values for each claim
    for claim in claims:
        templist = []
        claim_start, claim_dim = claim
        x, y = claim_start
        length, height = claim_dim
        x, y, length, height = map(int, [x, y, length, height])
        for i in range(height):
            for j in range(length):
                val = canvas1[y + i][x + j]
                templist.append(val)
        # check templist for all 1's
        if templist.count(1) == len(templist):
            print(templist)
            print("unconflicted claim found!")
            unconflicted_claim = [[str(x), str(y)], [str(length), str(height)]]
            print(unconflicted_claim)
    return unconflicted_claim


def main():
    input_file = "day3input.txt"
    input_path = Path.cwd() / "inputs" / input_file
    with input_path.open('r') as claim_file:
        claims = [line.strip() for line in claim_file]
    canvas = []
    for row in range(1000):
        canvas.append([])
        for col in range(1000):
            canvas[row].append(0)
    canvas1, cleaned_claims = overlap(canvas, claims)
    canvas1_flat = flatten(canvas1)
    overlaps = 0
    for num in range(2, max(canvas1_flat) + 1):
        overlaps += canvas1_flat.count(num)
    print(f"number of overlaps: {overlaps}\n")

    unconflicted_claim = find_claim(canvas1, cleaned_claims)
    claim_id = claims.index(unconflicted_claim) + 1
    print(f"ID of unconflicted claim: {claim_id}")
    return


if __name__ == '__main__':
    main()
