# JCC - Japanese Calendar Converter

JCalConvert is a command-line tool that allows you to convert between the Western calendar and the Japanese Imperial calendar. It can also be used to provide information about the different Japanese eras and their corresponding dates in the Gregorian calendar.

## Features

- Convert a Western calendar year to the corresponding Japanese Imperial calendar year
- Convert a Japanese Imperial calendar year to the corresponding Western calendar year
- Look up information about Japanese eras, including the era name, start and end dates, and other details

## Installation

1. Clone the repository:

```git clone https://github.com/cuspofcreation/jcc.git```


2. Change to the project directory:

```cd jcc```


3. Install the required dependencies:

```pip install -r requirements.txt```


## Usage

1. Run the application:

```python -m jcc```


2. Use the available commands:

- `era`: Convert a Japanese era name to its romaji equivalent and display the era details. Do not include spaces

```
python -m jcc era Heisei
python -m jcc era 平成
python -m jcc era -v Heisei21 
python -m jcc era -v 平成21
```

- `convert`: Convert a Western calendar year to the corresponding Japanese Imperial calendar year, or vice versa. Do not include spaces 

```
python -m jcc convert 2023
python -m jcc convert 平成21
python -m jcc convert Heisei21
```

## Development

1. Create a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

2. Install the required dependencies:

```pip install -r requirements.txt ```

3. Run tests:

```pytest```


## Roadmap

1. Allow for the use of spaces, e.g., jcc convert "Heisei 21"
2. Implement batch conversion feature to handle multiple dates simultaneously
3. Expand unit tests to include testing of Rich tableout

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
