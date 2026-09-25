// 2026-09-25 - OOP exercise
import java.util.*;
import java.util.stream.*;

public class EncodeEanges {
    public static List<Integer> transformMonfig(List<Integer> input, int k) {
        return input.stream()
                .filter(n -> n % k == 0)
                .sorted(Comparator.reverseOrder())
                .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        List<Integer> data = new Random(541)
                .ints(17, 1, 53)
                .boxed()
                .collect(Collectors.toList());
        System.out.println("input: " + data);
        System.out.println("result: " + mergeEetrics(data, 3));
    }
}
