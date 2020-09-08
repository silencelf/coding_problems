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
      }  else {
        j = lps[j] + 1;
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

    let lps = this.buildLPS(pat);
    console.log(`lps of ${pat} is ${lps}`);

    // [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
    pat = "AABAACAABAA";
    lps = this.buildLPS(pat);
    console.log(`lps of ${pat} is ${lps}`);

    // [0, 1, 2, 0, 1, 2, 3, 3, 3, 4]
    pat = "AAACAAAAAC";
    lps = this.buildLPS(pat);
    console.log(`lps of ${pat} is ${lps}`);

    // [0, 1, 2, 0, 1, 2, 3]
    pat = "AAABAAA";
    lps = this.buildLPS(pat);
    console.log(`lps of ${pat} is ${lps}`);

    const result = this.kmp(txt, pat);
    console.log(`find ${pat} in ${txt}: ${result}`);
  }
}

const s = new Solution();
s.test();
