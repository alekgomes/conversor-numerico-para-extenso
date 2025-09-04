# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python project that converts numeric numbers to their Portuguese text representation (e.g., 32 → "trinta e dois"). The project was inspired by a coding interview challenge.

## Commands

### CLI Usage
```bash
# Convert a number to text
python main.py 32
# Output: trinta e dois

./main.py 155
# Output: cento e cinquenta e cinco

# Show help
python main.py --help
```

### Running Tests
```bash
python main.py --test
# Or run tests directly
python test_conversor.py
```

### Running Individual Tests
```bash
python -m unittest test_conversor.test_unidades
python -m unittest test_conversor.test_dezenas  
python -m unittest test_conversor.test_centenas
```

## Architecture

The project is now split into three Python files:

- **conversor.py**: Core conversion logic
  - **Numero class**: Main converter class that handles number-to-text conversion
    - Takes a numeric input in constructor and converts to string
    - Separate methods for building units (`monta_unidade`), tens (`monta_dezena`, `monta_dezena_2`), and hundreds (`monta_centena`)
    - Main conversion logic in `escrever()` method that handles different number lengths (1-3 digits)

- **main.py**: CLI interface
  - Command-line argument parsing with argparse
  - Error handling for out-of-range numbers (0-999)
  - Integration with test runner

- **test_conversor.py**: Unit tests
  - **test_conversor class**: Unit test class with comprehensive test coverage
    - `test_unidades`: Tests single digit conversion including zero
    - `test_dezenas`: Tests two-digit numbers including special cases (11-19)
    - `test_centenas`: Tests three-digit numbers including edge cases

- **conversor-poo.py**: Legacy single-file version (still functional)

## Key Implementation Details

- Currently supports numbers from 0-999
- Special handling for "eleven" pattern (11-19) with separate method `monta_dezena_2`
- Edge case handling for "cem" (100) vs "cento" (used in compound numbers)
- Uses Portuguese number naming conventions