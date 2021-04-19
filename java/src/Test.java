import java.util.*;

public class Test {

    static class Solution {
        static int[] p;
        static int N;
        static int[] answer;
        static int[] sales;
        static Map<String, Integer> enroll_dict;
        public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
            N = enroll.length;
            p = new int[N];
            answer = new int[N];
            sales = new int[N];
            enroll_dict = new HashMap<>();
            Arrays.fill(answer,0);
            Arrays.fill(sales,0);
            for(int i = 0 ; i<N;i++) {
                p[i] = i;
                enroll_dict.put(enroll[i],i);
            }
            for(int i = 0 ; i<N;i++){
                String refer = referral[i];
                if(refer.equals("-")) continue;
                p[i] = enroll_dict.get(refer);
            }
            for(int i = 0; i<seller.length;i++){
                String sell = seller[i];
                int money = amount[i]*100;
                sales[enroll_dict.get(sell)]+=money;
            }
            for(int i = 0; i<N;i++){
                splitMoney(sales[i],i);
            }
            return answer;
        }
        public void splitMoney(int money, int now){
            int reposit = money/10;
            if(reposit>0){
                answer[now]+=money-reposit;
                if(p[now]==now) return;
                splitMoney(reposit,p[now]);
            }else{
                answer[now]+=money;
            }
        }
    }
}
