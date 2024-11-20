def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()

    words = file_contents.split()

    letters = {}
    for char in file_contents.lower():
        if not char.isalpha():
            continue
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1

    print(f"--- Begin report of {path} ---")
    print(f"{len(words)} words found in the document")
    print()

    for letter in letters:
        print(f"The '{letter}' character was found {letters[letter]} times")

    print("--- End report ---")


main()

