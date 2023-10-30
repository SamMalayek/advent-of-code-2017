from functools import reduce


def main():
    lengths = [ord(c) for c in open('day10.txt', 'r').read().rstrip()]
    lengths.extend([17, 31, 73, 47, 23])

    sequence = [i for i in range(256)]
    n = len(sequence)
    i = 0
    skipSize = 0

    for _ in range(64):
        for length in lengths:
            if length > n:
                continue
            # Reverse the order of that length of elements,
            # starting with the element at i.
            # Note that this reversing is circular.
            end = (i + length) % n
            if i < end:
                sequence = sequence[:i] + sequence[i:end][::-1] + sequence[end:]
            elif i > end:
                wrappedSublist = sequence[i:] + sequence[:end]
                wrappedSublist.reverse()
                sequence[:end], sequence[i:] = wrappedSublist[n-i:], wrappedSublist[:n-i]

            # Move i forward by length + skip size
            i = (i + length + skipSize) % n

            # Increase skip size by 1
            skipSize += 1

    knotHashNums = []

    for i in range(0, len(sequence), 16):
        knotHashNums.append(reduce(lambda i, j: i ^ j, sequence[i:i+16]))

    knotHash = ''.join([hex(d)[2:].rjust(2, '0') for d in knotHashNums])

    print(knotHash)


main()
