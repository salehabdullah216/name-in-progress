import re
import argparse
import requests

def convert_nala_to_yay(input_text):
    # Split the input text by lines
    lines = input_text.strip().split('\n')
    
    # Define a regex pattern to match package names
    pattern = re.compile(r'^\S+')
    
    # Use list comprehension to extract package names, excluding lines that start with special characters
    packages = [pattern.match(line).group(0) for line in lines if pattern.match(line) and not line.startswith(('├──', '└──'))]
    
    return packages

def get_arch_package_name(debian_package_name):
    # Example function to query Arch Linux Package Search API
    url = f"https://archlinux.org/packages/search/json/?q={debian_package_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            return data['results'][0]['pkgname']
    return debian_package_name

def convert_packages_to_arch(packages):
    arch_packages = []
    for package in packages:
        arch_package = get_arch_package_name(package)
        arch_packages.append(arch_package)
    return arch_packages

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Convert Nala text to Yay format with package name conversion.')
    parser.add_argument('input_file', type=str, help='Path to the input text file')
    parser.add_argument('output_file', type=str, help='Path to the output text file')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Read the input file
    with open(args.input_file, 'r') as file:
        input_text = file.read()
    
    # Convert the text
    debian_packages = convert_nala_to_yay(input_text)
    
    # Convert Debian package names to Arch package names
    arch_packages = convert_packages_to_arch(debian_packages)
    
    # Format the package names into a sentence
    formatted_output = "The following packages are available: " + ", ".join(arch_packages) + "."
    
    # Write the formatted output to the output file
    with open(args.output_file, 'w') as file:
        file.write(formatted_output)

if __name__ == '__main__':
    main()
