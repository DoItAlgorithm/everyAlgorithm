```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    public static int[][] graph;
    public static boolean[][] visited;
    public static int n, l, r;
    public static class Pos{
        int x;
        int y;
        public Pos(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
    public static int[] dx = {1, -1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};

    // 국경선을 열고 국경선을 공유하는 나라들의 위치 리스트를 반환
    public static List<Pos> open(int x, int y){
        Queue<Pos> queue = new LinkedList<>();
        queue.offer(new Pos(x, y));
        LinkedList<Pos> list = new LinkedList<>();
        visited[x][y] = true;

        while (!queue.isEmpty()){
            Pos nowPos = queue.poll();
            int nowX = nowPos.x;
            int nowY = nowPos.y;
            int nowNum = graph[nowX][nowY];
            list.add(new Pos(nowX, nowY));

            for(int i=0; i<4; i++){
                int nx = nowX+dx[i];
                int ny = nowY+dy[i];
                if(0<=nx && nx<n && 0<=ny && ny<n && !visited[nx][ny]
                && l<=Math.abs(graph[nx][ny]-nowNum) && Math.abs(graph[nx][ny]-nowNum)<=r){
                    visited[nx][ny] = true;
                    queue.offer(new Pos(nx, ny));
                }
            }
        }
        return list;
    }

    // 인구 이동
    public static int move(List<Pos> list){
        int cnt = list.size();
        int sum = 0;
        for(Pos pos : list){
            sum += graph[pos.x][pos.y];
        }
        int avg = sum/cnt;

        for(Pos pos : list){
            graph[pos.x][pos.y] = avg;
        }
        return cnt;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.valueOf(st.nextToken());
        l = Integer.valueOf(st.nextToken());
        r = Integer.valueOf(st.nextToken());

        graph = new int[n][n];
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<n; j++){
                graph[i][j] = Integer.valueOf(st.nextToken());
            }
        }
        int day = 0;
        while (true){
            boolean flag = false;
            visited = new boolean[n][n];
            for(int i=0; i<n; i++){
                for(int j=0; j<n; j++){
                    if(!visited[i][j]){
                        List<Pos> list = open(i, j);
                        int num = move(list);
                        if (num>1)
                            flag=true;
                    }
                }
            }
            if(!flag)
                break;
            day++;
        }
        bw.write(String.valueOf(day));
        bw.flush();
        bw.close();
        br.close();
    }
}
```