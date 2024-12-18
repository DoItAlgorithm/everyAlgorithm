```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

    public static int isPalindrome(String str, int idx, int jdx, int cnt){
        if(cnt>1)
            return cnt;

        while (idx<jdx){
            if(str.charAt(idx)==str.charAt(jdx)){
                idx++;
                jdx--;
            }
            else{
                int temCnt1 = isPalindrome(str, idx+1, jdx, cnt+1);
                int temCnt2 = isPalindrome(str, idx, jdx-1, cnt+1);
                return Math.min(temCnt1, temCnt2);
            }
        }
        return cnt;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.valueOf(br.readLine());
        while (t-->0){
            String str = br.readLine();
            int len = str.length();
            int idx = 0;
            int jdx = len-1;
            int result = isPalindrome(str, idx, jdx, 0);
            bw.write(String.valueOf(result)+"\n");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
```