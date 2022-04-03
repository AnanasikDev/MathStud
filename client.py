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

starttime = time()

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
                          f"ALLOW_BASIC = {core.ALLOW_BASIC}\n"
                          f"ALLOW_EQUATION = {core.ALLOW_EQUATION}\n"
                          f"ALLOW_SQRT = {core.ALLOW_SQRT}\n"
                          "----------------")

                print("[cmd]: incorrect arguments format")

            else:

                if arguments[1] not in [true, false]:
                    print("[cmd]: incorrect arguments format")

                else:
                    value = {true : True, false : False}[arguments[1]]
                    if arguments[0] == "basic":
                        core.ALLOW_BASIC = value
                        print(f"[cmd]: set ALLOW_BASIC to {value}")
                    elif arguments[0] == "equation":
                        core.ALLOW_EQUATION = value
                        print(f"[cmd]: set ALLOW_EQUATION to {value}")
                    elif arguments[0] == "sqrt":
                        core.ALLOW_SQRT = value
                        print(f"[cmd]: set ALLOW_SQRT to {value}")
                    else:
                        print("[cmd]: incorrect command format")

        if command == "break":
            break

    elif i == str(answer):
        stats["correct"] += 1
        stats["total"] += 1
        stats["correct/total"] = stats["correct"] / stats["total"]
        print("Yes!")
    else:
        stats["total"] += 1
        stats["correct/total"] = stats["correct"] / stats["total"]
        print("No, correct answer is", answer)
