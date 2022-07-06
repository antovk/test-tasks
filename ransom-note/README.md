# ransom note (leetcode easy)

## Task

<pre>
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

</pre>

## Solution

```java
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> ransomNoteCharsCount = new HashMap<>();
        Map<Character, Integer> magazineCharsCount = new HashMap<>();

        for (int i = 0; i < ransomNote.length(); i++) {
            ransomNoteCharsCount.merge(ransomNote.charAt(i), 1, Integer::sum);
        }

        for (int i = 0; i < magazine.length(); i++) {
            magazineCharsCount.merge(magazine.charAt(i), 1, Integer::sum);
        }

        for (Character key : ransomNoteCharsCount.keySet()) {
            if (!magazineCharsCount.containsKey(key) || magazineCharsCount.get(key) < ransomNoteCharsCount.get(key)) {
                return false;
            }
        }
        return true;

    }
}
```
