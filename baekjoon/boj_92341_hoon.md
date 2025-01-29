```java
import java.util.*;
class Solution {
    
    // 시간 변환 메서드: HH:MM 형식을 분 단위로 변환
    public int transMinute(String time){
        int hour = Integer.valueOf(time.split(":")[0]);
        int min = Integer.valueOf(time.split(":")[1]);
        min += hour*60;
        return min;
    }
    
    public int[] solution(int[] fees, String[] records) {
        int basicTime = fees[0];
        int basicFee = fees[1]; 
        int unitTime = fees[2]; 
        int unitFee = fees[3]; 
        
        // 입차 기록과 누적 시간을 기록하는 맵
        HashMap<String, String> entryRecordMap = new HashMap<>();
        HashMap<String, Integer> cumParkingTimeMap = new HashMap<>(); 
        
        for(String record : records){
            String[] recordParts = record.split(" ");
            String time = recordParts[0];
            int minute = transMinute(time);
            String carNum = recordParts[1];
            String history = recordParts[2];
            
            if(history.equals("OUT")){
                int entranceTime = transMinute(entryRecordMap.get(carNum));
                cumParkingTimeMap.put(carNum, cumParkingTimeMap.getOrDefault(carNum, 0)+minute-entranceTime);
                entryRecordMap.remove(carNum);
            }
            else{
                entryRecordMap.put(carNum, time);
            }
        }
        
        // 23:59분에 출차된 차들 처리
        for(Map.Entry<String, String> entry : entryRecordMap.entrySet()){
            cumParkingTimeMap.put(entry.getKey(), cumParkingTimeMap.getOrDefault(entry.getKey(), 0)+transMinute("23:59")-transMinute(entry.getValue()));
        }
        
        // 차량 번호 정렬
        List<String> carNumList = new ArrayList<>();
        for(String carNum : cumParkingTimeMap.keySet()){
            carNumList.add(carNum);
        }
        Collections.sort(carNumList);
        
        // 계산
        int[] answer = new int[carNumList.size()];
        for(int i=0; i<carNumList.size(); i++){
            int time = cumParkingTimeMap.get(carNumList.get(i));
            if(time<=basicTime){
                answer[i] = basicFee;
            }
            else{
                int tem = (time-basicTime)%unitTime==0 ? (time-basicTime)/unitTime : (time-basicTime)/unitTime+1;
                answer[i] = basicFee + tem*unitFee;
            }
        }
        return answer;
    }
}
```