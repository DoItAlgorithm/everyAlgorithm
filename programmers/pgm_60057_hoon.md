```java
class Solution {
    public int solution(String s) {
        int strLen = s.length();
        int answer = strLen;
        
        for(int i=1; i<=strLen/2; i++){
            String temStr = s.substring(0, i);
            int len = i;
            int repeat = 1;
    
            for(int j=i; j<=strLen-i; j+=i){
                String curStr = s.substring(j, j+i);
                if(temStr.equals(curStr)){
                    if(repeat>1){
                        repeat++;
                        if(repeat==10 || repeat==100 || repeat == 1000)
                            len++;
                    }
                    else{
                        repeat++;
                        len+=1;
                    }
                }
                else{
                    temStr = curStr;
                    len += i;
                    repeat = 1;
                }
            }
            len += strLen%i;
            answer = Math.min(answer, len);
        }
        return answer;
    }
}

```