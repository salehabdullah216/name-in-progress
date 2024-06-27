# Nala to Yay Package Converter

This project provides a Python script and a Bash script to convert package names from a Nala text file to a format suitable for Yay, including converting Debian package names to Arch package names using the Arch Linux Package Search API.

## Prerequisites

- Python 3.x
- `requests` library for Python

You can install the `requests` library using pip:
```bash
pip install requests
```

## Files

- `convert_nala_to_yay_with_chatgpt.py`: The main Python script that performs the conversion.
- `run_conversion.sh`: A Bash script to execute the Python script with input and output file arguments.

## Usage

### Python Script

The Python script reads an input text file, extracts package names, converts Debian package names to Arch package names, and writes the formatted output to an output text file.

#### Command-line Arguments

- `input_file`: Path to the input text file containing Nala package information.
- `output_file`: Path to the output text file where the formatted package names will be written.

### Bash Script

The Bash script provides a convenient way to run the Python script with the required arguments.

#### Command-line Arguments

- `input_file`: Path to the input text file containing Nala package information.
- `output_file`: Path to the output text file where the formatted package names will be written.

### Steps to Execute

1. Save the Python script as `convert_nala_to_yay_with_chatgpt.py`.
2. Save the Bash script as `run_conversion.sh`.
3. Make the Bash script executable by running:
   ```bash
   chmod +x run_conversion.sh
   ```
4. Execute the Bash script with the input text file and specify the output text file:
   ```bash
   ./run_conversion.sh path/to/your/input_file.txt path/to/your/output_file.txt
   ```

### Example

```bash
./run_conversion.sh /home/saleh/Documents/code/installed_packages.txt /home/saleh/Documents/export.txt
```

## How It Works

1. **Extract Package Names**: The Python script reads the input text file and extracts package names using a regular expression.
2. **Convert Package Names**: It queries the Arch Linux Package Search API to find corresponding Arch package names for the extracted Debian package names.
3. **Format Output**: The script formats the package names into a sentence and writes the output to the specified output file.

## Notes

- **Arch Linux Package Search API**: The script uses a hypothetical API endpoint. You may need to adjust the URL and parsing logic based on the actual API documentation.
- **Error Handling**: Ensure proper error handling for network requests and JSON parsing.
- **Rate Limiting**: Be mindful of API rate limits and implement appropriate handling if necessary.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
