from datetime import date
from sys import exit
import inflect

def main():
    print(minutes(input("Day of Birth: ")))


def minutes(s):
    s = s.strip()
    src = s.split('-')
    p = inflect.engine()
    today = date.today()
    try:
        for item in src:
            if not item.isdigit():
                exit()
        birthday = date.fromisoformat(s)
        res = p.number_to_words((round((today - birthday).total_seconds() / 60)), andword="")
        result = res[0].title() + res[1:]
        return result + " minutes"

    except:
        print("Invalid date")
        exit(1)

if __name__ == "__main__":
    main()
