from typing import List


class Case:
    def __init__(self, input, expected):
        self.input = input
        self.expected = expected


class Result:
    def __init__(self, actual):
        self.actual = actual


class Solution:
    def __init__(self, solution):
        self.solution = solution

    def run(self, case: Case) -> Result:
        return self.solution(case)


class Challenge:
    challenges = []

    def __init__(self, challenge_name, solution: Solution, cases: List[Case]) -> None:
        self.challenge_name = challenge_name
        self.passed = False
        self.solution = solution
        self.cases = cases
        Challenge.challenges.append(self)

    @classmethod
    def get_challenges(cls) -> List["Challenge"]:
        return cls.challenges

    @classmethod
    def challenges_completed(cls):
        return len(cls.challenges)

    @classmethod
    def run_all(cls):
        for challenge in cls.challenges:
            challenge.run()

    def print_status(self) -> None:
        print(f"[{'x' if self.passed else ' '}] - Challenge: {self.challenge_name}")
        print(f"\t{self.solution.__doc__}")

    def run(self) -> None:
        passes = 0
        for case in self.cases:
            try:
                result = self.solution.run(case)
                if result.actual == case.expected:
                    passes += 1
                else:
                    raise AssertionError(
                        f"Expected: {case.expected}, Actual: {result.actual}"
                    )
            except Exception as error:
                print(f"FAIL: {error}")
        self.passed = passes == len(self.cases)
        self.print_status()
