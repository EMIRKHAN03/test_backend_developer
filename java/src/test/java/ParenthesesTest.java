import org.example.Parentheses;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class ParenthesesTest {
    @Test
    void basicTests() {
        assertEquals(1, Parentheses.countWellFormedParenthesis(1));
        assertEquals(5, Parentheses.countWellFormedParenthesis(3));
        assertEquals(42, Parentheses.countWellFormedParenthesis(5));
        assertEquals(9694845, Parentheses.countWellFormedParenthesis(15));
    }

    @Test
    void performanceTest() {
        long start = System.currentTimeMillis();
        int result = Parentheses.countWellFormedParenthesis(15);
        long duration = System.currentTimeMillis() - start;
        assertTrue(duration < 1000);
        assertEquals(9694845, result);
    }
}