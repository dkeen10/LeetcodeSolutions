package misc;

class Solution {
    public void reverseString(char[] s) {
        int i = 0;
        int j = s.length -1;
        while (i <= j) {
            char temp = s[i];
            s[i] = s[j];
            s[j] = temp;
            i++;
            j--;
        }
    }
}

// class Solution {
//     public void reverseString(char[] s) {
//         char temp;
//         for( int i = 0, j = s.length - 1; i <= j; j--, i++){
//             temp = s[i];
//             s[i] = s[j];
//             s[j] = temp;
//         }
//     }
// }