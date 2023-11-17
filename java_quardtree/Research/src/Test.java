import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
public class Test {
    public static void test1(){
        Map<Integer, Integer> test = new HashMap<>();
        test.put(1, 3);
        test.put(2, 5);
        test.put(6, 3);
        test.put(11, 1);
        // Now you can use querd0 or perform any other operations with it.
        int binsize = 5;
        Map<Integer, Integer> bins = new HashMap<>();
        for (int value : test.keySet()) {
            int floeCount = test.get(value);
            int binNum = value % binsize == 0 ? value / binsize : value / binsize + 1;
            int size = binNum * binsize;
            bins.put(size, bins.getOrDefault(size, 0) + floeCount);
        }

        List<Integer> sizes = new ArrayList<>(bins.keySet());
        sizes.sort(null);
        List<Integer> counts = new ArrayList<>();
        for (int size : sizes) {
            counts.add(bins.get(size));
        }
        System.out.println("sizes: " + sizes);
        System.out.println("counts: " + counts);
    }
}
