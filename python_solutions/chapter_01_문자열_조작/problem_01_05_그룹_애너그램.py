"""
Chapter 01 - Problem 05 - 그룹 애너그램 - https://leetcode.com/problems/group-anagrams/

문제 설명:
문자열 배열을 받아 애너그램 단위로 그룹핑하라.

예제:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

풀이: 애너그램을 저장하기 위해 defaultdict로 anagrams를 생성합니다. defaultdict는 키가 없는 경우에도 기본값으로 빈 리스트([])를 반환하므로, 애너그램 그룹을 저장하기에 적합합니다.

그런 다음, 주어진 단어 리스트를 순회하면서 애너그램을 그룹화합니다. 각 단어를 정렬하여 키로 사용하고, 해당 키에 해당하는 애너그램 그룹에 단어를 추가합니다. 이를 위해 defaultdict의 list 메서드인 append를 사용합니다.

모든 단어를 처리한 후, anagrams의 값들을 리스트로 변환하여 반환합니다. 이때, anagrams.values()를 사용하면 애너그램 그룹들을 가져올 수 있습니다.
"""

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # 애너그램을 저장하기 위한 defaultdict를 생성합니다.
    # keyerror 방지: defaultdict는 키가 없는 경우 기본값으로 빈리스트([])를 반환
    anagrams = collections.defaultdict(list)

    # 주어진 단어 리스트를 순회하면서 애너그램을 그룹화합니다.
    for word in strs:
        # 단어를 정렬하여 키로 사용하고, 해당 키에 해당하는 애너그램 그룹에 단어를 추가합니다.
        anagrams[''.join(sorted(word))].append(word)
    # 애너그램 그룹들을 리스트로 변환하여 반환합니다.
    return list(anagrams.values())