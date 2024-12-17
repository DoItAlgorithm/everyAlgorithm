```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.valueOf(st.nextToken());
        int K = Integer.valueOf(st.nextToken());

        String str = br.readLine();
        Stack<Integer> stack = new Stack<>();

        for(int i=0; i<N; i++){
            int num = Integer.valueOf(str.charAt(i)-'0');
            while (!stack.isEmpty() && stack.peek()<num && K>0){
                stack.pop();
                K--;
            }
            stack.push(num);
        }

        while (K-->0){
            stack.pop();
        }

        for(int x: stack){
            bw.write(String.valueOf(x));
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
```