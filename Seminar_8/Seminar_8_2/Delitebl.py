


# def delit(number):
#     with open("phone_data.csv", "r", encoding="utf-8") as f:
#         lines = f.readlines()
#     with open("phone_data.csv", "w", encoding="utf-8") as f:
#         f.writelines
#         replace(f[number], '')

def delit(number):
    number = int(number - 1)
    with open("phone_data.csv", "r+", encoding='utf-8') as f:
        lines = f.read().splitlines()
        lines.pop(number)

    with open("phone_data.csv", "w", encoding='utf-8') as f:
        f.write('\n'.join(lines) +'\n')
        print('\n'.join(lines))