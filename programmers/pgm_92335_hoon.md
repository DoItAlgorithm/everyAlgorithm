```java
import java.util.*;

class Solution {
    
    // 소수 판별 메서드
    public boolean checkPrime(String chunkStr){
        if(chunkStr.isEmpty() || chunkStr.equals("1"))
            return false;
        
        // 오버플로우 때문에 long 타입을 사용해야 함.
        long chunkNum = Long.valueOf(chunkStr);
        
        for(int i=2; i<=(int)(Math.sqrt(chunkNum)); i++){
           if(chunkNum%i==0){
               return false;
           } 
        }
        return true;
    }
    
    public int solution(int n, int k) {
        String radixNum = Integer.toString(n, k);
        int len = radixNum.length();
        
        int idx = 0;
        int answer = 0;
        StringBuilder sb = new StringBuilder();
        
        // 진법 변환 결과 문자열을 순차적으로 탐색하며
        for(int jdx=0; jdx<len; jdx++){
            
            // '0'이 아닌 문자는 누적하고,
            if(radixNum.charAt(jdx)!='0'){
                sb.append(radixNum.charAt(jdx));
            }
            // '0'이 나오면 누적된 문자열을 소수 판별합니다.
            else{
                if(checkPrime(sb.toString()))
                    answer++;
                sb.delete(0, sb.length());
            }
        }
        
        if(checkPrime(sb.toString())){
            answer++;
        }
        
        return answer;
    }
}
```