from shared import Challenge, Case, Result, Solution


def solution(case: Case):
    print(str(case))
    return Result(actual="")


solution1 = Solution(solution)

case1 = Case(input="", expected="")
case2 = Case(input="", expected="")

challenge_1 = Challenge(
    challenge_name="challenge 1", solution=solution1, cases=[case1, case2]
)
