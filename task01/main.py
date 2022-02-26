import sys

ENCRYPTION_CYCLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 "

pseudo_sys_argv_1 = list(["e", "ABC", "1"])
pseudo_sys_argv_2 = list(["e", "ABCrererDFSF879", "61"])
pseudo_sys_argv_3 = list(["d", "Khoor zruog", "3"])


def chiffre(e_d: str, shift: int) -> None:
    result = []
    for i in range(0, len(e_d)):
        for j in range(0, len(ENCRYPTION_CYCLE)):
            if e_d[i] == ENCRYPTION_CYCLE[j]:
                result.append(ENCRYPTION_CYCLE[(j + shift) % len(ENCRYPTION_CYCLE)])
                break
    print("".join(result))


def main(pseudo_sys_argv: list) -> None:
    key = int(pseudo_sys_argv[2])
    if "e" == pseudo_sys_argv[0]:
        chiffre(pseudo_sys_argv[1], key)
    elif pseudo_sys_argv[0] == "d":
        chiffre(pseudo_sys_argv[1], -key)
    else:
        sys.exit("Invalid argument. Use 'e' or 'd'")


if __name__ == '__main__':
    main(pseudo_sys_argv_1)
    main(pseudo_sys_argv_2)
    main(pseudo_sys_argv_3)
