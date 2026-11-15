
***

**Prepare your files:**
   *   `text.txt` — Paste your story or text here. Each line will be printed separately.
   *   `speed_of_text.txt` — Enter the delay (in seconds) for each line. Each value must be on a new line (e.g., `0.1`, `0.5`, `1.0`).
   *   *Note: The number of lines in both files must match.*

3. **Run the script:**
    ```bash
    python main.py
    ```

##  How It Works

The core logic relies on Python's `zip()` function to iterate through two files simultaneously. It pairs a line of text with its corresponding delay, then passes them to a custom `print_smooth()` function that outputs characters with a short delay to achieve the typewriter effect.

## Example

**text.txt:**
```text
Hello, world!
Welcome to AutoQ.
This is a test.
```

**speed_of_text.txt:**
```text
0.05
0.1
0.2
```

##  Author

**Kernel (Kok0-Chan)**
*   GitHub: [@Kok0-Chan](https://github.com/Kok0-Chan)
```
