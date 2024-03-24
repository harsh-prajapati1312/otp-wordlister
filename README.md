# OTP Wordlister

![Banner](
  ██████  ████████ ██████        ██     ██  ██████  ██████  ██████  ██      ██ ███████ ████████ ███████ ██████
██    ██    ██    ██   ██       ██     ██ ██    ██ ██   ██ ██   ██ ██      ██ ██         ██    ██      ██   ██
██    ██    ██    ██████  █████ ██  █  ██ ██    ██ ██████  ██   ██ ██      ██ ███████    ██    █████   ██████
██    ██    ██    ██            ██ ███ ██ ██    ██ ██   ██ ██   ██ ██      ██      ██    ██    ██      ██   ██
 ██████     ██    ██             ███ ███   ██████  ██   ██ ██████  ███████ ██ ███████    ██    ███████ ██   ██



)

Generate wordlists of integers with specified lengths for One-Time Password (OTP) applications.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [Contributing](#contributing)
- [License](#license)

## Introduction

OTP Wordlister is a command-line tool designed to generate wordlists of integers tailored for OTP applications. These wordlists can be useful for testing and security purposes, such as testing the strength of OTP systems or performing brute-force attacks (only for lawful and ethical purposes).

## Features

- Generate wordlists of integers with custom lengths.
- Support for verbose mode to display progress during wordlist generation.
- Support for wizard mode for guided setup.
- Easy-to-use command-line interface.

## Installation

To install OTP Wordlister, follow these steps:

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/otp-wordlister.git
    ```

2. Navigate to the directory:

    ```sh
    cd otp-wordlister
    ```

3. Install dependencies (if any):

    ```sh
    pip install -r requirements.txt
    ```

## Usage

To use OTP Wordlister, follow these steps:

1. Open a terminal.

2. Navigate to the directory where OTP Wordlister is installed.

3. Run the script with the desired options. For example:

    ```sh
    python otp_wordlister.py -d 4 -o wordlist.txt
    ```

## Options

- `-d`, `--digits`: Specify the number of digits for integers in the wordlist.
- `-o`, `--output`: Specify the output file name for the wordlist.
- `-v`, `--verbose`: Enable verbose mode to display progress during wordlist generation.
- `--wizard`: Enable wizard mode for guided setup.

## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/yourfeature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/yourfeature`).
6. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Disclaimer**: This tool is intended for lawful and ethical use only. Users are responsible for complying with applicable laws and regulations.
