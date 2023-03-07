# defining the shift count
shipt=3
encrypted_text = "YJJWF"

plain_text = ""

for c in encrypted_text:

    # check if character is an uppercase letter
    if c.isupper():

        # find the position in 0-25
        c_unicode = ord(c)

        c_index = ord(c) - ord("A")

        # perform the negative shift
        new_index = (c_index - shipt) % 26

        # convert to new character
        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        # append to plain string
        plain_text = plain_text + new_character

    else:

        # since character is not uppercase, leave it as it is
        plain_text += c

print("Encrypted text:",encrypted_text)

print("Decrypted text:",plain_text)