import re


def get_skype_name(test_string: str, masks_char: str) -> str:

    get_format_name = re.search(r'skype:\w+', test_string)
    if get_format_name:
        new_string = re.sub(r'skype:\w+', 'skype:' + masks_char, test_string)
        return new_string
    print('Username is not correct format')
    return test_string


def get_phone_number(test_string: str, count_hidden_digits: int, masks_char: str) -> str:

    phone_numbers = re.findall(r'[+]\d\d \d\d\d \d\d\d \d\d\d', test_string)
    if count_hidden_digits == 0 and len(test_string) > 1:
        print('Count hidden digits = 0 (warning)')
        return test_string
    elif count_hidden_digits > 11 or len(test_string) < 1:
        print('Count hidden digits > 11 or string is empty (warning)')
        return test_string

    new_string = test_string
    count_spaces = count_hidden_digits // 3
    for phone_number in phone_numbers:
        hidden_number = phone_number[:-count_hidden_digits-count_spaces] + count_hidden_digits % 3 * masks_char + \
            count_spaces * (' ' + 3 * masks_char)
        new_string = new_string.replace(phone_number, hidden_number)
    return new_string


def get_email(test_string: str, masks_char: str) -> str:
    try:
        email_without_domain = re.findall(r'(\S+)@', test_string)
        first_char = re.findall(r'^\w', email_without_domain[0])
        last_char = re.findall(r'\w$', email_without_domain[0])

        email_domain = re.findall(r'@(\S+)', test_string)
        first_char_domain = re.findall(r'^\w', email_domain[0])
        last_char_domain = re.findall(r'\w$', email_domain[0])

        if (first_char and last_char) and (first_char_domain and last_char_domain):
            search_email = re.search(r'\w+[-.+_]\w+@\w+\.\w+', test_string).group(0)
            split_email = search_email.split('@')
            email_without_domain, email_domain = split_email[0], split_email[1]
            hidden_email = email_without_domain[0] + str(len(email_without_domain[0:-1]) * masks_char) + \
                email_without_domain[-1]
            new_email = hidden_email + '@' + email_domain
            result_string = test_string.replace(search_email, new_email)
            return result_string
        else:
            print('The first and the last character of username/domain are incorrect format (warning)')
            return test_string
    except AttributeError:
        print("Wrong format of data (warning)")
        return test_string
    except IndexError:
        print('List index out of range. Data is not correct (warning)')
        return test_string


if __name__ == '__main__':

    # Check skype:number
    string = input('(INPUT) String value: ')
    mask_char = input('(INPUT) Mask value: ')
    print(f'(OUTPUT) {get_skype_name(string, mask_char)}')

    # Check  phone number
    # string = input('(INPUT) String value: ')
    # count_digits = int(input('(INPUT) Count of  digits: '))
    # mask_char = input('(INPUT) Mask value: ')
    # try:
    #     print(f'(OUTPUT) {get_phone_number(string, count_digits, mask_char)}')
    # except TypeError:
    #     print("Incorrect type of data. Please, input again")

    # # Check email
    # string = input('(INPUT) String value: ')
    # count_digits = int(input('(INPUT) Count of  digits: '))
    # masks_char = input('(INPUT) Mask value: ')
    # try:
    #     print(f'(OUTPUT) {get_email(string,  masks_char)}')
    # except TypeError:
    #     print("Incorrect type of data. Please, input again")
    #
    #




















