from collections import deque


def check(skill, st):
    skill = deque(skill)
    for c in st:
        if c in skill and c != skill.popleft():
            return 0
    return 1


def solution(skill, skill_trees):
    cnt = 0
    for st in skill_trees:
        cnt += check(skill, st)

    return cnt


Skill = "CBD"
Skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(Skill, Skill_trees))
