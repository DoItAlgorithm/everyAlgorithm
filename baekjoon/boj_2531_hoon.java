```java
import java.io.*;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];
        for(int i=0; i<N; i++){
            int num = Integer.parseInt(br.readLine());
            arr[i] = num;
        }

        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(c, 1);
        for(int i=0; i<k; i++){
            map.put(arr[i], map.getOrDefault(arr[i], 0)+1);
        }
        int maxType = map.size();

        int idx = k;
        for(int i=idx; i<N+k; i++){
            // 다시 원점 돌아오면 반복문 탈출
            if(i%N==k-1)
                break;
            map.put(arr[i%N], map.getOrDefault(arr[i%N], 0)+1);
            map.put(arr[(i-k+N)%N], map.get(arr[(i-k+N)%N])-1);
            if(map.get(arr[(i-k+N)%N])==0)
                map.remove(arr[(i-k+N)%N]);
            maxType = Math.max(maxType, map.size());
        }
        System.out.println(maxType);
    }
}
```