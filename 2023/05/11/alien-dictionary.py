from collections import defaultdict, deque


class Solution:
    def findOrder(self, alien_dict, N, K):
        outgoingSetMap = defaultdict(set)
        incomingCount = [0] * 26

        for word in alien_dict:
            for letter in word:
                outgoingSetMap[letter] = set()

        for i in range(len(alien_dict) - 1):
            curr_word = alien_dict[i]
            next_word = alien_dict[i+1]
            counter = 0
            while (counter < len(curr_word) and counter < len(next_word)):
                curr_letter = curr_word[counter]
                next_letter = next_word[counter]

                if curr_letter != next_letter:
                    if next_letter not in outgoingSetMap[curr_letter]:
                        outgoingSetMap[curr_letter].add(next_letter)
                        incomingCount[ord(next_letter) - ord('a')] += 1
                    break
                else:
                    counter += 1

        letter_order = []
        temp = []
        for letter in (outgoingSetMap.keys()):
            if incomingCount[ord(letter) - ord("a")] == 0:
                temp.append(letter)

        stage = deque(set(temp))
        while (stage):
            current_letter = stage.popleft()
            letter_order.append(current_letter)
            for child in outgoingSetMap[current_letter]:
                incomingCount[ord(child) - ord('a')] -= 1
                if (incomingCount[ord(child) - ord('a')] == 0):
                    stage.append(child)
        return ''.join(letter_order)

tests = [
    # ['abc'],
    # ['a', 'ab'],
    # ['a', 'ab', 'abc'],
    # ['ba', 'baad', 'da', 'efh', 'efz'],
    "bf biifablhhfekcjfhdklefkiihffedfjkklldcbfdldddbf bikjidjifidghfklddjchiebjbibdjadlgji bkblijbgjbkillhcblbjacadceahebbcafichcjedhbajlfkei bldgbfhkfdbcihbdkfejkdgikeclih cbielkdheejdicfjfeclbdliidkdcfifdgehlleikkdb cccfckhbglgfi cjjgibfkgegchldfaclliejhhcbjickadahbcdkialldfb eclbbfcjdfecfdkiblddaceclddfkaabjgalgiggacjdegf efdjhebdfebhhccahifhaififjbadhc eghcflfgkllde eidbdkcjicecjaiddfdcjkfj ejifhhdiclkkejdhidkhbhjdihbdkckfkgiidhadjdje elacahafeeghdgkic fag fbeidhlbfhcbjebaegidflileilejkijdfjdkiclabdfjeejeg gebfadchbgcikgkfifaga gialjghjjhhedflkkdjlhajdkhdakhadkkajgllgllbghk helekchjgeb iehdjcjefggkcafllgedfhjhhiahgc ike ikgjliklfblbagfafe ilfeajblklchcebejiggjhfbdcla jdlfbhdfjbdblgcceihcgiaachlhlhjhcglhcaf jeahcekiahlkidflijakdj jfhgbkchhgckahefbjcgaceibkiehallgiffddchacigefa jhlfhckghgkgfb kfcahfciklbakdgehkgfadggdcjcfaijkjlffjf kiidkhfcclldfceahaabjfgdi kjbchgcbbdghhk lfkdjkkeebibdidhjfkldkhecllebheehjhcaileeggafii lhd lkkkldcfbfekbjdfalhiddaiegkf lljjjgj".split()
    # ['a', 'ba', 'cbc']
]

for test in tests:
    print(f"Test: {test}")
    print(f"Ans: {Solution().findOrder(test,1,1)}")
    print()
