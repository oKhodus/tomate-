import time as t

def tomate_timer(work_minutes, break_minutes, cycles = 4):
    for cycle in range(1, cycles + 1):
        print(f"Cycle {cycle}/{cycles}: work time is - {work_minutes}")
        t.sleep(work_minutes * 60)
        print("Break time!")
        t.sleep(break_minutes * 60)
    print("That's all the work is done, good job!")

if __name__ == "__main__":
    work_time = int(input("Enter duration of your work (in minutes): "))
    break_time = int(input("Enter duration of your break (in minutes): "))
    tomate_timer(work_time, break_time)