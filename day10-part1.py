
def main():
    lengths = list(map(int, open('day10.txt', 'r').read().rstrip().split(',')))

    sequence = [i for i in range(256)]
    n = len(sequence)
    i = 0
    skipSize = 0

    for length in lengths:
        if length > n:
            continue
        # Reverse the order of that length of elements,
        # starting with the element at i.
        # Note that this reversing is circular.
        end = (i + length) % n
        if i < end:
            sequence = sequence[:i] + sequence[i:end][::-1] + sequence[end:]
        elif i == end:
            pass
        else:
            wrappedSublist = sequence[i:] + sequence[:end]
            wrappedSublist.reverse()
            sequence[:end], sequence[i:] = wrappedSublist[n-i:], wrappedSublist[:n-i]

        # Move i forward by length + skip size
        i = (i + length + skipSize) % n

        # Increase skip size by 1
        skipSize += 1

    print(sequence[0] * sequence[1])


main()
