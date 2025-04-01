def compress_string(s):
    if not s:
        return "    "

    compressed = "  "
    count = 1
    current_char = s[0]

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed += current_char
            if count > 1:
                compressed += str(count)
            current_char = s[i]
            count = 1

    # Add the last character and its count (if any)
    compressed += current_char
    if count > 1:
        compressed += str(count)

    return compressed

# Example usage:
input_string = input("Enter a string: ")
compressed_string = compress_string(input_string)
print(compressed_string)