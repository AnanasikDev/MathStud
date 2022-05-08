import MathCore as core
from time import time

true = "true"
false = "false"

level = 2
stats = {

    "correct" : 0,
    "correct/total" : 0,
    "total" : 0,
    "elapsed" : 0

}

print(f"Super Mega Math Game started! Level = {level}. Use /help to get all commands")
print("================")

starttime = time()


def allow(arguments, value):
    if arguments[0] == "basic":
        core.Allows["ALLOW_BASIC"] = value
        print(f"[cmd]: set ALLOW_BASIC to {value}")
    elif arguments[0] == "equation":
        core.Allows["ALLOW_EQUATION"] = value
        print(f"[cmd]: set ALLOW_EQUATION to {value}")
    elif arguments[0] == "sqrt":
        core.Allows["ALLOW_SQRT"] = value
        print(f"[cmd]: set ALLOW_SQRT to {value}")
    elif arguments[0] == "expression":
        core.Allows["ALLOW_EXPRESSION"] = value
        print(f"[cmd]: set ALLOW_EXPRESSION to {value}")
    elif arguments[0] == "view":
        core.Allows["ALLOW_VIEW"] = value
        print(f"[cmd]: set ALLOW_VIEW to {value}")
    elif arguments[0] == "quadratic_equation":
        core.Allows["ALLOW_QUADRATIC_EQUATION"] = value
        print(f"[cmd]: set ALLOW_QUADRATIC_EQUATION to {value}")
    elif arguments[0] == "measure":
        core.Allows["ALLOW_MEASURE"] = value
        print(f"[cmd]: set ALLOW_MEASURE to {value}")
    else:
        print("[cmd]: incorrect command format")


while True:

    answer = core.generate(level)
    i = input()

    if i.startswith("/"):
        cmd = i[1::].split()

        command = cmd[0]
        arguments = cmd[1::]

        if command == "help":
            print("----All commands----\n"
                  "/help - invoke this help window\n"
                  "/getlevel - returns current level\n"
                  "/setlevel - {arg} sets level to {arg}\n"
                  "/break - stops the game\n"
                  "/allow {arg0} {arg1} - sets arg0 to arg1. arg0: basic / equation / sqrt / expression / view / quadratic_equation / measure; arg1: true / false\n"
                  "/allowonly {arg} arg: basic / equation / sqrt / expression / view / quadratic_equation / measure"
                  "/allow - returns current permissions settings\n"
                  "/stats - returns your stats by this session\n"
                  "--------------------")

        if command == "setlevel":
            if level <= 0:
                print(f"[cmd]: wrong level value")
            else:
                level = int(arguments[0])
                print(f"[cmd]: level changed to {level}")

        if command == "stats":
            stats["elapsed"] = round(time() - starttime)
            print(f"----Statistics----\n"
                  f"correct : {stats['correct']} ({round(stats['correct/total']*100, 5)}%)\n"
                  f"total : {stats['total']}\n"
                  f"time elapsed : {stats['elapsed']}s\n"
                  f"------------------")

        if command == "getlevel":
            print(f"[cmd]: current level is {level}")

        if command == "allow":

            if len(arguments) != 2:

                if len(arguments) == 0:
                    print("----Settings----\n"
                          f"ALLOW_BASIC = {core.Allows['ALLOW_BASIC']}\n"
                          f"ALLOW_EQUATION = {core.Allows['ALLOW_EQUATION']}\n"
                          f"ALLOW_SQRT = {core.Allows['ALLOW_SQRT']}\n"
                          f"ALLOW_EXPRESSION = {core.Allows['ALLOW_EXPRESSION']}\n"
                          f"ALLOW_VIEW = {core.Allows['ALLOW_VIEW']}\n"
                          f"ALLOW_QUADRATIC_EQUATION = {core.Allows['ALLOW_QUADRATIC_EQUATION']}\n"
                          f"ALLOW_MEASURE = {core.Allows['ALLOW_MEASURE']}\n"
                          "----------------")
                else:
                    print("[cmd]: incorrect arguments format")

            else:

                if arguments[1] not in [true, false]:
                    print("[cmd]: incorrect arguments format")

                else:
                    value = {true : True, false : False}[arguments[1]]
                    allow(arguments, value)

        if command == "allowonly":
            for i in core.Allows.keys():
                core.Allows[i] = False
            allow(arguments, True)

        if command == "break":
            break

    elif i in answer:
        stats["correct"] += 1
        stats["total"] += 1
        stats["correct/total"] = stats["correct"] / stats["total"]
        print("Yes!")
        print("================")
    else:
        stats["total"] += 1
        stats["correct/total"] = stats["correct"] / stats["total"]
        print("No, the correct answer is", answer[0])
        print("================")
