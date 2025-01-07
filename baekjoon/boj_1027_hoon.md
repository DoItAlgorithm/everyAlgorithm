```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // 해당 문제에서 기울기의 절대값의 최대값은 10억
        final int INF = 1000000001;
        int answer = 0;

        for(int i=0; i<n; i++){
            int cnt = 0;

            // 왼쪽 구간에서 최소 기울기의 갱신 횟수 계산
            double minValue = (double)(INF);
            for(int j=i-1; j>=0; j--){
                double slope = ((double)(arr[i]-arr[j]))/(i-j);
                if(slope<minValue){
                    cnt++;
                    minValue = slope;
                }
            }

            // 오른쪽 구간에서 최대 기울기의 갱신 횟수 계산
            double maxValue = (double)(-INF);
            for(int j=i+1; j<n; j++){
                double slope = ((double)(arr[j]-arr[i]))/(j-i);
                if(slope>maxValue){
                    cnt++;
                    maxValue = slope;
                }
            }
            answer = Math.max(answer, cnt);
        }
        System.out.println(answer);
    }
}
```