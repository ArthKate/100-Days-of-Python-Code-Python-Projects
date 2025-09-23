# Caesar Cipher
Simple README explaining the caesar_cipher.py solution.

## Description
The script implements a Caesar cipher: each alphabetic character in the input is shifted by a fixed number of positions. Case is preserved and non-letter characters (spaces, punctuation, numbers) are left unchanged. Shifts wrap around the alphabet (e.g., shifting 'z' by 1 yields 'a').

## API / Usage
- Function (example): `caesar(text, shift, direction='encode')`
    - text: string to transform
    - shift: integer number of positions to shift (positive for right)
    - direction: `'encode'` to encrypt or `'decode'` to reverse

Example in Python:
```
from caesar_cipher import caesar

encrypted = caesar("Hello, World!", 5, direction="encode")
original  = caesar(encrypted, 5, direction="decode")
```

If the script provides a command-line interface, typical usage would be:
```
python caesar_cipher.py --text "Hello" --shift 3 --direction encode
```

## Algorithm notes
- Only letters A–Z and a–z are shifted.
- Case preserved by applying shift within each case range.
- Non-letter characters are returned unchanged.
- Shift values larger than 26 are handled by modulo arithmetic.

## Testing
Try small examples to verify behavior:
- `caesar("abc", 2)` -> `"cde"`
- `caesar("xyz", 3)` -> `"abc"`
- `caesar("Hello!", 5, "decode")` -> reversed transformation of prior encode

## License
Include a license of your choice if sharing publicly.
