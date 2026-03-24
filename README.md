# Simple Text Input Output Tester

A simple Python application that reads text from `stdin` and echoes it back to `stdout`. This tool is useful for testing text handling, stream processing, and basic input/output behavior in Python environments.

## Features

- **Real-time Echoing**: Processes and echoes input line by line.
- **Support for Multi-line Input**: Handles continuous streams of text.
- **Robustness**: Includes basic error handling for `EOFError` and `KeyboardInterrupt`.

## Requirements

- Python 3.x

## Project Structure

- `app.py`: The main application script.
- `test_app.py`: Test script to verify the application's functionality.
- `README.md`: This documentation file.

## Usage

To run the application manually:

```bash
python3 app.py
```

After running the command, you can type any text and press `Enter`. The application will echo your input back to the terminal. To exit, press `Ctrl+D` (EOF) or `Ctrl+C`.

### Example

```bash
$ python3 app.py
Hello World
Hello World
This is a test.
This is a test.
```

## Testing

The project includes a basic test suite to ensure the echo functionality works as expected.

To run the tests:

```bash
python3 test_app.py
```

The test script runs `app.py` as a subprocess, provides it with sample input, and verifies that the output matches the input exactly.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue if you find a bug or have a suggestion for improvement.

## License

This project is open-source and available under the MIT License.
