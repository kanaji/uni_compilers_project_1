from myparser import parser_check

if __name__ == "__main__":
    x = input('Enter input string: ')
    print(f'Input string: {x}, string length: {len(x)}')
    print(f'State: {parser_check(x)}')
