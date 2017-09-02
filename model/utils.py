import random
import string
import re

def random_string(prefix, max_len):
    # symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for _ in range(random.randrange(max_len))])

def random_email(prefix, max_len):
    username_symbols = string.ascii_letters + string.digits + "+._"
    username = prefix + "".join([random.choice(username_symbols) for _ in range(random.randrange(int(max_len/2-2)))])

    domain_symbols = string.ascii_letters + string.digits + "._"
    domain= "".join([random.choice(domain_symbols) for _ in range(random.randrange(int(max_len/2-3)))])

    tld_symbols = string.ascii_letters + string.digits
    tld = "".join([random.choice(tld_symbols) for _ in range(random.randrange(3))])

    return "{}@{}.{}".format(username, domain, tld)

def random_phone(prefix, max_len):
    symbols = string.digits + "()+_ "
    return prefix + "".join([random.choice(symbols) for _ in range(random.randrange(max_len))])

def trim_spaces(string):
    return re.sub(" +", " ", string).strip(" ")

def cleanup_phone_string(phone):
    return re.sub("[() -]", "", phone) if phone else ""

def cleanup_email_string(email):
    return trim_spaces(email)
