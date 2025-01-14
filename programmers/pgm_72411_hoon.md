```java
import java.util.*;
class Solution {
    
    // 특정 단품 개수에 따른 조합을 구하는 메서드
    public void findCombination(int idx, int curCnt, int goalCnt, char[] chArr, HashMap<String, Integer> map, StringBuilder tem){
        
        if(curCnt==goalCnt){
            map.put(tem.toString(), map.getOrDefault(tem.toString(), 0)+1);
            return;
        }
        
        for(int i=idx,len = chArr.length; i<len; i++){
            tem.append(chArr[i]);
            findCombination(i+1, curCnt+1, goalCnt, chArr, map, tem);
            tem.deleteCharAt(tem.length()-1);
        }
        
    }
    
    public List<String> solution(String[] orders, int[] course) {
        // 정답 문자열 리스트
        List<String> answer = new ArrayList<>();
        
        for(int cnt : course){
            HashMap<String, Integer> map = new HashMap<>();
            for(String order : orders){
                char[] chArr = order.toCharArray();
                Arrays.sort(chArr);
                findCombination(0, 0, cnt, chArr, map, new StringBuilder());
            }
            
            // 가장 많이 함께 주문된 단품 메뉴 조합 구하기
            int maxSize = 0;
            List<String> temList = new ArrayList<>();
            for(Map.Entry<String, Integer> entry : map.entrySet()){
                if(entry.getValue()>maxSize){
                    temList.clear();
                    maxSize = entry.getValue();
                    temList.add(entry.getKey());
                }
                else if(entry.getValue()==maxSize){
                    temList.add(entry.getKey());
                }
            }
            
            // 2명 미만의 손님으로부터 주문시 skip
            if(maxSize<2)
                continue;

            for(int i=0, size = temList.size(); i<size; i++){
                answer.add(temList.get(i));
            }
        }
        Collections.sort(answer);
        return answer;
    }
}
```