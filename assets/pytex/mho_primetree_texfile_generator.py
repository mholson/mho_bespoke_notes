from pathlib import Path

path_home = Path.home()
path_sub = "Library/CloudStorage/Dropbox/assets/pytex"
path_python = path_home / path_sub


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


for integer in range(4, 1001):
    if is_prime(integer):
        pass
    else:
        with open(
            f"{path_python}/imgs_pytex_primetree-{integer}.tex", "a", encoding="utf-8"
        ) as the_file:
            the_file.write(rf"\documentclass[crop, varwidth]{{standalone}}" "\n")
            the_file.write(rf"\input{{mho_pythontex_factortree}}" "\n")
            the_file.write(rf"\begin{{document}}" "\n")
            the_file.write(rf"\PrimeTree{{{integer}}}" "\n")
            the_file.write(rf"\end{{document}}")
