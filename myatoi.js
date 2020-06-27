// initial version
var myAtoi = function(str) {
    var valid = false;
    var dict = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    };
    var result = 0;
    var sign = 1;
    for(var c of str) {
        if (!valid && c == ' ')
            continue;
        if (!valid && (!dict.hasOwnProperty(c) && c !== '-' && c !== '+'))
            return 0;
        if (valid && !dict.hasOwnProperty(c))
            break;
        if (!valid && c === '-') {
            sign = -1;
            valid = true;
        }
        if (!valid && dict.hasOwnProperty(c))
            valid = true;
        if (!valid && c === '+')
            valid = true;
        if (dict.hasOwnProperty(c))
            result = result * 10 + dict[c];
    }

    if (result >= Math.pow(2, 31))
        return sign == 1 ? Math.pow(2, 31) - 1: sign * Math.pow(2, 31);

    return sign*result;
};

console.log(myAtoi("+1"));
console.log(myAtoi("+556 other words"));
console.log(myAtoi("-556"));
