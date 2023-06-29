"""
Chapter 01 - Problem 03 - 로그 파일 재정렬 - https://leetcode.com/problems/reorder-data-in-log-files/

문제 설명:
로그를 재정렬하라. 기준은 다음과 같다.
1. 로그의 가장 앞 부분은 식별자다
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.

예제:
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

풀이: 주어진 로그 리스트를 letters와 digits라는 두 개의 리스트로 분리합니다. 

이후, 반복문을 통해 각 로그를 확인합니다. 로그를 공백으로 분리한 후, 두 번째 단어가 숫자인지 확인하여 숫자 로그인 경우 digits 리스트에 추가합니다. 그렇지 않은 경우에는 문자 로그로 간주하여 letters 리스트에 추가합니다.

문자 로그인 letters 리스트를 정렬합니다. 정렬 기준은 람다 표현식으로 지정되는데, 먼저 두 번째 단어부터 마지막까지를 기준으로 오름차순 정렬하고, 동일한 경우 첫 번째 단어를 기준으로 오름차순 정렬합니다. 이를 위해 key 매개변수에 람다 표현식을 사용하여 정렬 기준을 지정합니다.

마지막으로, 정렬된 letters 리스트와 digits 리스트를 합쳐서 반환합니다. 

"""

def reorderLogFiles(self, logs: List[str]) -> List[str]:
    letters, digits = [], [] # 문자 로그와 숫자 로그를 구분하기 위한 빈 리스트를 선언합니다.
    for log in logs:
        if log.split()[1].isdigit(): # 로그의 두 번쨰 단어가 숫자인지 확인합니다.
            digits.append(log) # 숫자 로그일 경우 digits 리스트에 추가
        else:
            letters.append(log) # 문자 로그일 경우 letters 리스트에 추가
    
    # 문자 로그를 정렬합니다.
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits;