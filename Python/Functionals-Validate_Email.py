import re

def fun(s):
    # return True if s is a valid email, else return False
    return re.match("(\w|\-)+@[0-9a-zA-Z]+\.[a-zA-Z]{1,3}$", s) is not None
    
def filter_mail(emails):
    return filter(fun, emails)

if __name__ == '__main__':
    n = int(raw_input())
    emails = []
    for _ in range(n):
        emails.append(raw_input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print filtered_emails
