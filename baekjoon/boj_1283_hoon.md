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
        HashSet<Character> set = new HashSet<>();
        while (n-->0){
            String str = br.readLine();
            String[] words = str.split(" ");

            StringBuilder sb = new StringBuilder();

            // 1. 단어의 첫 글자 검사
            // isChecked가 true면 단어의 첫 글자가 지정됬음을 의미
            boolean isChecked = false;
            for(String word : words){
                char firstCh = word.charAt(0);
                if(isChecked){
                   sb.append(word).append(" ");
                }
                else{
                    if(set.contains(Character.toLowerCase(word.charAt(0)))){
                        sb.append(word).append(" ");
                    }
                    else{
                        set.add(Character.toLowerCase(firstCh));
                        isChecked = true;
                        sb.append("[").append(firstCh).append("]").append(word.substring(1, word.length())).append(" ");
                    }
                }
            }

            // 2. 왼쪽부터 순차 탐색
            if(!isChecked){
                for(int i=0; i< str.length(); i++){
                    char ch = str.charAt(i);
                    if(ch==' ')
                        continue;
                    else if(!set.contains(Character.toLowerCase(ch))){
                        set.add(Character.toLowerCase(ch));
                        sb.insert(i, '[');
                        sb.insert(i+2, ']');
                        break;
                    }
                }
            }

            bw.write(sb.toString().trim()+"\n");

        }

        bw.flush();
        bw.close();
        br.close();
    }
}
```