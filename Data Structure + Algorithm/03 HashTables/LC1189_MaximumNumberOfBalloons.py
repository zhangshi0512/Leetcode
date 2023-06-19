"""
1189. Maximum Number of Balloons

Given a string text, you want to use the characters of text 
to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. 
Return the maximum number of instances that can be formed.

Example 1:

Input: text = "nlaebolko"
Output: 1

Example 2:

Input: text = "loonbalxballpoon"
Output: 2

Example 3:

Input: text = "leetcode"
Output: 0
"""

def maxNumberOfBalloons(text):
    # 创建一个字典用来存储text中每个字符的频率
    char_dict = dict()
    for c in text:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1

    # 定义一个集合来存储单词"balloon"的字符
    balloon = set(list("balloon"))

    # 创建一个新的字典来存储"balloon"中每个字符在text中的频率
    count_dict = dict()
    for balloon_char in balloon:
        if not balloon_char in char_dict:
            # 如果"balloon"中的字符在text中不存在，那么返回0，因为不能形成"balloon"
            return 0
        else:
            # 如果"balloon"中的字符在text中存在，那么存储其频率
            count_dict[balloon_char] = char_dict[balloon_char]

    # 创建一个列表来存储"balloon"中每个字符可以形成的"balloon"的数量
    count_list = []
    for c in count_dict:
        if c in ['a', 'b', 'n']:
            # 对于字符'a'、'b'和'n'，它们在"balloon"中出现一次，所以直接添加其数量
            count_list.append(count_dict[c])
        else:
            # 对于字符'l'和'o'，它们在"balloon"中出现两次，所以添加其数量的一半（整数除法）
            count_list.append(count_dict[c] // 2)

    # 返回可以形成"balloon"的最大数量，这就是列表中的最小值
    return min(count_list)


print(1, maxNumberOfBalloons("nlaebolko"))
print(2, maxNumberOfBalloons("loonbalxballpoon"))
print(0, maxNumberOfBalloons("leetcode"))
print()

def maxNumberOfBalloons2(text):
    # 创建一个字典，键是"balloon"中的字符，值是0
    # 初始化"balloon"中每个字符的数量为0
    count = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

    # 计算text中"balloon"中每个字符的数量
    for char in text:
        if char in count:
            count[char] += 1

    # 计算可以形成多少个"balloon"
    # 字母'b'、'a'、'n'在"balloon"中出现一次
    # 字母'l'、'o'在"balloon"中出现两次
    count['l'] //= 2
    count['o'] //= 2

    # 返回可以形成的"balloon"的最大数量
    return min(count.values())

