module.exports.countWellFormedParenthesis = function (n) {
    const memo = new Array(n + 1).fill(0);
    memo[0] = 1;
    for (let i = 1; i <= n; i++) {
        for (let j = 0; j < i; j++) {
            memo[i] += memo[j] * memo[i - j - 1];
        }
    }
    return memo[n];
}

module.exports = { countWellFormedParenthesis };