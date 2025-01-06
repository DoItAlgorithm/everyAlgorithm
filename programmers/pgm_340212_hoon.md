```java
class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        
        int low = 1;
        int high = 100000;
        int answer = high;
        
        while(low<=high){
            int level = (low+high)/2;
            long totalTime = 0;
            for(int i=0; i<diffs.length; i++){
                if(diffs[i]<=level || i==0){
                    totalTime += times[i];
                }
                else{
                    totalTime +=  (long)(diffs[i]-level)*(times[i]+times[i-1])+times[i];
                }
            }
            
            if(totalTime>limit){
                low = level+1;
            }
            else{
                high = level-1;
                answer = Math.min(answer, level);
            }
        }
        
        return answer;
        
    }
}
```