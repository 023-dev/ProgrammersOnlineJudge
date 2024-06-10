import java.util.ArrayList;
class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        ArrayList<Integer> w = new ArrayList<>();
        ArrayList<Integer> h = new ArrayList<>();
        for (int i = 0; i < sizes.length; i++) {
            if (sizes[i][0] < sizes[i][1]) {
                w.add(sizes[i][1]);
                h.add(sizes[i][0]);
            } else {
                w.add(sizes[i][0]);
                h.add(sizes[i][1]);
            }
        }
        w.sort(Integer::compareTo);
        h.sort(Integer::compareTo);
        answer = w.get(w.toArray().length-1) * h.get(h.toArray().length-1);
        return answer;
    }
}