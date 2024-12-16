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

        int n = Integer.valueOf(br.readLine());
        int m = Integer.valueOf(br.readLine());
        String s = br.readLine();
        HashMap<Character, Integer> map = new HashMap<>();
        int result = 0;
        for(int i=0; i<m; i++){
            char ch = s.charAt(i);
            map.put(ch, map.getOrDefault(ch, 0)+1);
            int iCnt = map.getOrDefault('I', 0);
            int oCnt = map.getOrDefault('O', 0);

            if(ch=='I'){
                if(iCnt==oCnt+1 && oCnt>=n){
                    result++;
                }
                else{
                    map.clear();
                    map.put('I', 1);
                }
            }
            if(ch=='O'){
                if(iCnt!=oCnt){
                    map.clear();
                }
            }
        }
        bw.write(String.valueOf(result));

        bw.flush();
        bw.close();
        br.close();
    }
}
```