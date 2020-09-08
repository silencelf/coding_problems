#!/usr/bin/node

class Solution {
  kmp(text, pattern) {
    const lps = this.buildLPS(pattern);

    let i = 0;
    let j = 0;
    while (i < text.length && j < pattern.length) {
      if (text[i] === pattern[j]) {
        i++;
        j++;
      } else if (j) {
        j = lps[j - 1];
      } else {
        i++;
      }
    }

    if (j === pattern.length) 
      return i - j;

    return -1;
  }

  /*
   * this one is difficult
   */
  buildLPS(txt) {
    let len = 0;
    const lps = [0];
    let i = 1;
    while ( i < txt.length) {
      if (txt[i] === txt[len]) {
        len++;
        lps.push(len);
        i++;
      } else if (len != 0) {
          len = lps[len - 1];
      } else {
          lps.push(0);
          i++;
      }
    }

    return lps;
  }

  test() {
    let txt = 'AAAAABAAABA';
    let pat = 'AAAA';
    let result = null;

    result = this.kmp(txt, pat);
    console.log(`find ${pat} in ${txt}: ${result}`);

    txt = 'hello';
    pat = 'll';
    result = this.kmp(txt, pat);
    console.log(`find ${pat} in ${txt}: ${result}`);

    txt = 'abaaa';
    pat = 'abb';
    result = this.kmp(txt, pat);
    console.log(`find ${pat} in ${txt}: ${result}`);

    txt = 'mississippi';
    pat = 'issip';

    result = this.kmp(txt, pat);
    console.log(`find ${pat} in ${txt}: ${result}`);
  }
}

const s = new Solution();
s.test();
