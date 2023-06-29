"""
Chapter 01 - Problem 04 - 가장 흔한 단어 - https://leetcode.com/problems/most-common-word/

문제 설명:
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.

예제:
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]

Output: "ball"

풀이: 주어진 문단을 정규표현식을 통해 단어만 분리하고, 소문자로 변환한 뒤, banned 리스트에 포함되지 않는 단어만 추출하여 words 리스트에 저장합니다. 그리고 단어의 등장 횟수를 세기 위해 collections.Counter 객체인 counts를 생성합니다.

마지막으로, counts.most_common(1)을 호출하여 등장 횟수가 가장 많은 단어 1개를 튜플 형태로 반환하고, 그 중 첫 번째 원소인 단어를 반환합니다.

"""
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    # 정규 표현식을 사용하여 단어로 분리하고, 소문자로 변환한 뒤 banned 리스트에 포함되지 않는 단어만 추출합니다.
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    # 단어의 등장 횟수를 세기 위해 Counter 객체를 생성합니다.
    counts = collections.Counter(words)
        # 가장 빈도수가 높은 단어를 반환합니다. most_common(1)은 등장 횟수가 가장 많은 단어 1개를 튜플 형태로 반환합니다.  ex: [('ball', 2)]
    return counts.most_common(1)[0][0]