import re
import argparse
import requests

def convert_nala_to_yay(input_text):
    """Convert Nala formatted text to a list of package names."""
    lines = input_text.strip().split('\n')
    pattern = re.compile(r'^\S+')
    
    packages = [pattern.match(line).group(0) for line in lines if pattern.match(line) and not line.startswith(('├──', '└──'))]
    return packages

def get_arch_package_name(debian_package_name):
    """Query Arch Linux Package Search API to get the Arch package name for a given Debian package name."""
    url = f"https://archlinux.org/packages/search/json/?q={debian_package_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data['results']:
            return data['results'][0]['pkgname']
    except requests.RequestException as e:
        print(f"Error fetching package name for {debian_package_name}: {e}")
    return debian_package_name

def convert_packages_to_arch(packages):
    """Convert a list of Debian package names to Arch package names."""
    arch_packages = []
    for package in packages:
        arch_package = get_arch_package_name(package)
        arch_packages.append(arch_package)
    return arch_packages

def main():
    """Main function to parse arguments, convert package names, and write the output to a file."""
    parser = argparse.ArgumentParser(description='Convert Nala text to Yay format with package name conversion.')
    parser.add_argument('input_file', type=str, help='Path to the input text file')
    parser.add_argument('output_file', type=str, help='Path to the output text file')
    
    args = parser.parse_args()
    
    try:
        with open(args.input_file, 'r') as file:
            input_text = file.read()
    except IOError as e:
        print(f"Error reading input file: {e}")
        return
    
    debian_packages = convert_nala_to_yay(input_text)
    arch_packages = convert_packages_to_arch(debian_packages)
    
    formatted_output = "The following packages are available: " + ", ".join(arch_packages) + "."
    
    try:
        with open(args.output_file, 'w') as file:
            file.write(formatted_output)
    except IOError as e:
        print(f"Error writing to output file: {e}")

if __name__ == '__main__':
    main()
