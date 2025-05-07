const assert = require('assert');
const { countWellFormedParenthesis } = require('./parentheses');

describe('Parentheses', function () {
    it('Basic cases', function () {
        assert.strictEqual(countWellFormedParenthesis(1), 1);
        assert.strictEqual(countWellFormedParenthesis(3), 5);
        assert.strictEqual(countWellFormedParenthesis(5), 42);
        assert.strictEqual(countWellFormedParenthesis(15), 9694845);
    });

    it('Performance test', function () {
        const start = Date.now();
        const result = countWellFormedParenthesis(15);
        const duration = Date.now() - start;
        assert.ok(duration < 1000);
        assert.strictEqual(result, 9694845);
    });
});