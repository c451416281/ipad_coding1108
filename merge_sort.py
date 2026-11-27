"""Read a string and print its characters in sorted order."""


def merge_sort(text: str) -> str:
    """Return the characters in *text* sorted by their Unicode code points."""
    if len(text) <= 1:
        return text

    middle = len(text) // 2
    left = merge_sort(text[:middle])
    right = merge_sort(text[middle:])

    merged = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return "".join(merged)


if __name__ == "__main__":
    value = input("Enter a string: ")
    print(merge_sort(value))
