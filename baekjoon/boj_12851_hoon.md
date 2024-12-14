```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {

    public static class Pos{
        int x;
        int t;

        public Pos(int x, int t){
            this.x = x;
            this.t = t;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.valueOf(st.nextToken());
        int k = Integer.valueOf(st.nextToken());

        int[] timeArr = new int[Math.max(2*k+1, 2*n+1)];
        Arrays.fill(timeArr, -1);

        Queue<Pos> queue = new LinkedList<>();
        queue.add(new Pos(n, 0));
        timeArr[n] = 0;

        int shortestTime = Integer.MAX_VALUE;
        int cnt = 0;
        while (!queue.isEmpty()) {
            Pos nowPos = queue.poll();
            int nowX = nowPos.x;
            int nowT = nowPos.t;

            if (nowX == k) {
                if (shortestTime > nowT) {
                    shortestTime = nowT;
                    cnt = 1;
                } else {
                    cnt++;
                }
                continue;
            }

            if (nowX - 1 >= 0) {
                if (timeArr[nowX - 1] == -1 || timeArr[nowX - 1] == nowT + 1) {
                    timeArr[nowX - 1] = nowT + 1;
                    queue.offer(new Pos(nowX - 1, nowT + 1));
                }
            }
            if (nowX <= k - 1) {
                if (timeArr[nowX * 2] == -1 || timeArr[nowX * 2] == nowT + 1) {
                    timeArr[nowX * 2] = nowT + 1;
                    queue.offer(new Pos(nowX * 2, nowT + 1));
                }
            }
            if (nowX + 1 <= k) {
                if (timeArr[nowX + 1] == -1 || timeArr[nowX + 1] == nowT + 1) {
                    timeArr[nowX + 1] = nowT + 1;
                    queue.offer(new Pos(nowX + 1, nowT + 1));
                }
            }
        }

        bw.write(String.valueOf(shortestTime) + "\n");
        bw.write(String.valueOf(cnt));
        bw.flush();
        bw.close();
        br.close();
    }
}
```

