import argparse

def generate_wordlist(length, output_file, verbose):
    min_num = 10 ** (length - 1)
    max_num = (10 ** length) - 1
    with open(output_file, "w") as file:
        for num in range(min_num, max_num + 1):
            file.write(str(num) + "\n")
            if verbose:
                print(f"Generated: {num}", end='\r')
    if verbose:
        print("\nWordlist generation completed.")

def main():
    parser = argparse.ArgumentParser(description="Generate a wordlist of integers with a specified number of digits.")
    parser.add_argument("-d", "--digits", type=int, help="Number of digits for integers in the wordlist", required=True)
    parser.add_argument("-o", "--output", help="Output file name for the wordlist", required=True)
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode")
    parser.add_argument("--wizard", action="store_true", help="Enable wizard mode")
    args = parser.parse_args()

    if args.wizard:
        args.digits = int(input("Enter the number of digits for integers in the wordlist: "))
        args.output = input("Enter the output file name for the wordlist: ")
    
    generate_wordlist(args.digits, args.output, args.verbose)
    print(f"Wordlist of {args.digits}-digit numbers has been created successfully in '{args.output}'.")

if __name__ == "__main__":
    banner = """
\033[92m
  ██████  ████████ ██████        ██     ██  ██████  ██████  ██████  ██      ██ ███████ ████████ ███████ ██████  
██    ██    ██    ██   ██       ██     ██ ██    ██ ██   ██ ██   ██ ██      ██ ██         ██    ██      ██   ██ 
██    ██    ██    ██████  █████ ██  █  ██ ██    ██ ██████  ██   ██ ██      ██ ███████    ██    █████   ██████  
██    ██    ██    ██            ██ ███ ██ ██    ██ ██   ██ ██   ██ ██      ██      ██    ██    ██      ██   ██ 
 ██████     ██    ██             ███ ███   ██████  ██   ██ ██████  ███████ ██ ███████    ██    ███████ ██   ██ 
                                                                                                               
\033[0m
    \033[4mGitHub:\033[0m https://github.com//otp-wordlister
"""


    print(banner)
    main()
