import re


def combo_operand(register, operand):
    combo_dict = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": register[0],
        "5": register[1],
        "6": register[2],
        "7": None,
    }
    return combo_dict[str(operand)]


def get_instruction(k):
    opcode_dict = {
        "0": adv,
        "1": bxl,
        "2": bst,
        "3": jnz,
        "4": bxc,
        "5": out,
        "6": bdv,
        "7": cdv,
    }
    return opcode_dict[str(k)]


def adv(k, register, operand, i, output):
    register[0] = int(register[0] / 2 ** combo_operand(register, operand))
    return k, register, output


def bxl(k, register, operand, i, output):
    register[1] = register[1] ^ operand
    return k, register, output


def bst(k, register, operand, i, output):
    register[1] = combo_operand(register, operand) % 8
    return k, register, output


def jnz(k, register, operand, i, output):
    if register[0] != 0:
        k = operand - 1
    return k, register, output


def bxc(k, register, operand, i, output):
    register[1] = register[1] ^ register[2]
    return k, register, output


def out(k, register, operand, i, output):
    output.append(combo_operand(register, operand) % 8)
    return k, register, output


def bdv(k, register, operand, i, output):
    register[1] = int(register[0] / 2 ** combo_operand(register, operand))
    return k, register, output


def cdv(k, register, operand, i, output):
    register[2] = int(register[0] / 2 ** combo_operand(register, operand))
    return k, register, output


def main():
    data = []
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f]

    register = [int(re.findall(r"\d+", data[d])[0]) for d in range(3)]
    program = [int(p) for p in re.findall(r"\d+", data[4])]
    output = []

    k = 0
    while k < len(program) // 2:
        i = program[2 * k]  # instruction
        o = program[2 * k + 1]  # operand
        instruction = get_instruction(i)
        k, register, output = instruction(k, register, o, i, output)
        k += 1

    print(",".join(str(o) for o in output))


if __name__ == "__main__":
    main()
