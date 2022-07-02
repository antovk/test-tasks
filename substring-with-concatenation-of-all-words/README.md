# substring with concatenation of all words (leetcode red)

## Task

<pre>
You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]

Constraints:

1 <= s.length <= 104
s consists of lower-case English letters.
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] consists of lower-case English letters.
</pre>

---

## Solution

I assume that the words in the input string S can be different lengths, unlike the array of words.

```java
class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<>();
        int wordsArrayLength = words.length;
        int singleWordLength = words[0].length();
        Arrays.sort(words);

        for (int i = 0; i <= s.length() - wordsArrayLength * singleWordLength; i++) {
            String window = s.substring(i, i + wordsArrayLength * singleWordLength);
            boolean containsAll = true;

            List<String> substrSeparate = new ArrayList<>();

            for (String word : words) {
                if (!window.contains(word)) {
                    containsAll = false;
                    break;
                }
            }

            if (!containsAll) {
                continue;
            }

            for (int j = 0; j < wordsArrayLength; j++) {
                substrSeparate.add(window.substring(j * singleWordLength, j * singleWordLength + singleWordLength));
            }

            substrSeparate.sort((s1, str) -> s1.compareToIgnoreCase(str));

            if (Arrays.equals(words, substrSeparate.toArray(new String[0]))) {
                result.add(i);
            }
        }
        return result;
    }
}
```
