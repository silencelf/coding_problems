#!/usr/local/bin/node

class Solution {
  kmp(text, pattern) {
    return -1;
  }

  buildlps(txt) {
    if (!txt)
      return [];

    const lps = [0];
    for (let i = 1; i < txt.length; i++) {
      let j = 0;
      while (j < i) {
        if (txt[j] !== txt[i - j])
          break;
        j++;
      }
      lps.push(j);
    }

    return lps;
  }

  test() {
    let txt = 'AAAAABAAABA';
    let pat = 'AAAA';

    let lps = this.buildlps(pat);
    console.log(`lps of ${pat} is ${lps}`);

    // [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
    pat = "AABAACAABAA";
    lps = this.buildlps(pat);
    console.log(`lps of ${pat} is ${lps}`);

    // [0, 1, 2, 0, 1, 2, 3, 3, 3, 4]
    pat = "AAACAAAAAC";
    lps = this.buildlps(pat);
    console.log(`lps of ${pat} is ${lps}`);

    // [0, 1, 2, 0, 1, 2, 3]
    pat = "AAABAAA";
    lps = this.buildlps(pat);
    console.log(`lps of ${pat} is ${lps}`);

    const result = this.kmp(txt, pat);
    console.log(`find ${pat} in ${txt}: ${result}`);
  }
}

const s = new Solution();
s.test();
