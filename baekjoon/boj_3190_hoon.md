```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {

    public static class Pos{
        int x;
        int y;
        public Pos(int x, int y){
            this.x = x;
            this.y = y;
        }
    }

    public static class Dir{
        int time;
        char dir;
        public Dir(int time, char dir){
            this.time = time;
            this.dir = dir;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.valueOf(br.readLine());
        int[][] graph = new int[n][n];
        boolean[][] visited = new boolean[n][n];

        int k = Integer.valueOf(br.readLine());
        Queue<Pos> queue = new LinkedList<>();
        for(int i=0; i<k; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.valueOf(st.nextToken())-1;
            int y = Integer.valueOf(st.nextToken())-1;
            graph[x][y] = 1;
        }

        int l = Integer.valueOf(br.readLine());
        List<Dir> directions = new ArrayList<>();
        for(int i=0; i<l; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.valueOf(st.nextToken());
            char c = st.nextToken().charAt(0);
            directions.add(new Dir(x, c));
        }
        int time = 0;
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};
        int x = 0;
        int y = 0;
        int curDir = 1;
        int dirIdx = 0;
        visited[x][y]=true;
        queue.offer(new Pos(x, y));
        while(true){
            time++;
            x += dx[curDir];
            y += dy[curDir];
            queue.offer(new Pos(x, y));

            if(x<0 || x>=n || y<0 || y>=n || visited[x][y]){
                break;
            }
            visited[x][y] = true;
            if(graph[x][y]==1){
                graph[x][y] = 0;
            }
            else {
                Pos nowPos = queue.poll();
                visited[nowPos.x][nowPos.y] = false;
            }

            if (dirIdx < directions.size() && directions.get(dirIdx).time == time) {
                char turnDir = directions.get(dirIdx).dir;
                if (turnDir == 'L') {
                    curDir = (curDir - 1 + 4) % 4;
                } else {
                    curDir = (curDir + 1) % 4;
                }
                dirIdx++;
            }
        }
        bw.write(String.valueOf(time));


        bw.flush();
        bw.close();
        br.close();
    }
}
```