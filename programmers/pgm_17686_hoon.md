```java
import java.util.*;

class Solution {
    
    public class File implements Comparable<File>{
        int idx;
        String head;
        String number;
        String tail;
        
        public File(int idx, String head, String number, String tail){
            this.idx = idx;
            this.head = head;
            this.number = number;
            this.tail = tail;
        }
        
        // 커스텀 정렬 기준 구현
        @Override
        public int compareTo(File f){
            String headA = this.head.toUpperCase();
            String headB = f.head.toUpperCase();
            
            if(headA.equals(headB)){
                Integer numA = Integer.valueOf(this.number);
                Integer numB = Integer.valueOf(f.number);
                if(numA==numB){
                    return this.idx-f.idx;
                }
                else{
                    return numA-numB;
                }
            }
            else{
                return headA.compareTo(headB);
            }
        }
    }
    
    public String[] solution(String[] files) {
        
        List<File> fileList = new ArrayList<>();
        
        for(int i=0; i<files.length; i++){
            String file = files[i];
            StringBuilder headSb = new StringBuilder();
            StringBuilder numberSb = new StringBuilder();
            StringBuilder tailSb = new StringBuilder();
            int idx = 0;
            
            // 1. Head 분리
            while(idx<file.length()){
                char ch = file.charAt(idx);
                if(!Character.isDigit(ch)){
                    headSb.append(ch);
                }
                else{
                    break;
                }
                idx++;
            }
            
            // 2. Number 분리
            while(idx<file.length()){
                char ch = file.charAt(idx);
                if(Character.isDigit(ch)){
                    numberSb.append(ch);
                }
                else{
                    break;
                }
                idx++;
            }
            
            // 3. Tail 분리
            while(idx<file.length()){
                char ch = file.charAt(idx);
                tailSb.append(ch);
                idx++;
            }
            
            fileList.add(new File(i, headSb.toString(), numberSb.toString(), tailSb.toString()));
        }
        
        Collections.sort(fileList);
        
        String[] result = new String[files.length];
        for(int i=0; i<files.length; i++){
            File file = fileList.get(i);
            result[i] = file.head + file.number + file.tail;
        }

        return result;
    }
}
```

