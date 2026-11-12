def solution(myString):
    answer = []
    
    unit = ""
    
    for s in myString:
        if s != "x":
            unit += s
        else:
            if unit == "":
                continue
            answer.append(unit)
            unit = ""
    
    if unit != "":
        answer.append(unit)
    
    answer.sort()
    
    return answer
