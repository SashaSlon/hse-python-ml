#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def reverse_dictionary(dictionary):
    """
    Function reverses dictionary with structure { key: [values] } to
    dictionary with structure {value: [keys]}.

    >>> d = reverse_dictionary({1: [4], 2: [3]})
    >>> d == {3: [2], 4: [1]}
    True
    >>> d = reverse_dictionary({1: [3, 4, 5]})
    >>> d == {3: [1], 4: [1], 5: [1]}
    True
    >>> d = {'hello': ['привет', 'здравствуй'], 'python': ['питон']}
    >>> d = reverse_dictionary(d)
    >>> d == {'здравствуй': ['hello'],
    ... 'привет': ['hello'], 'питон': ['python']}
    True
    """
    result = {}
    for key, values in dictionary.items():
        for value in values:
            if value not in result:
                result[value] = [key]
            else:
                result[value].append(key)
    return result


def parse_dictionary(text):
    """
    Function forms dictionary from input text.

    >>> d = parse_dictionary('мама - mommy')
    >>> d == {'мама': ['mommy']}
    True
    >>> d = parse_dictionary('hello - привет, здравствуй')
    >>> d == {'hello': ['привет', 'здравствуй']}
    True
    >>> d = parse_dictionary('hello - привет, здравствуй, здорова')
    >>> d == {'hello': ['привет', 'здравствуй', 'здорова']}
    True
    >>> d = parse_dictionary("мама - mommy, mom\\nпапа - daddy, father")
    >>> d == {'мама': ['mommy', 'mom'], 'папа': ['daddy', 'father']}
    True
    >>> d = parse_dictionary("сын - son\\nпапа - daddy, father")
    >>> d == {'сын': ['son'], 'папа': ['daddy', 'father']}
    True
    """
    result = {}
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue

        key, values = line.split('-')
        key = key.strip()

        values = [val.strip() for val in values.split(',')]
        result[key] = values

    return result


def print_dictionary(dictionary):
    for key in sorted(dictionary):
        print(key + ' - ' + ', '.join(dictionary[key]))


def main():
    text = sys.stdin.read()
    base_dictionary = parse_dictionary(text)
    reversed_dictionary = reverse_dictionary(base_dictionary)
    print_dictionary(reversed_dictionary)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
