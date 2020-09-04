def solution(record):
    answer = []
    id_dic = {}
    for r in record:
        arr = list(r.split())
        if arr[0] in ["Enter", "Change"]:
            id_dic[arr[1]] = arr[2]
    for r in record:
        arr = list(r.split())
        if arr[0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(id_dic[arr[1]]))
        elif arr[0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(id_dic[arr[1]]))
    return answer


Record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(Record))
