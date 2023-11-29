katz_deli = ['Jon', 'jim', 'joe', 'joj']

def line(katz_deli):
    if katz_deli == []:
        return "The line is currently empty."
    elif katz_deli != []:
        line_status = "The line is currently:"
        for index, name in enumerate(katz_deli, start=1):
            line_status += f" {index}. {name}"
        print(line_status)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    return f"Welcome, {name}. You are number {len(katz_deli)} in line."

def now_serving(katz_deli):
        if not katz_deli:
            print("There is nobody waiting to be served!")
        else:
            name = katz_deli.pop(0)
            print(f"Currently serving {name}.")
    

print(now_serving(katz_deli))
print(line(katz_deli))
print(take_a_number(katz_deli, 'Ada'))