import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_2632 {
    static StringTokenizer st;
    static int[] pA, pB;
    static int[] pizzaA, pizzaB;
    static int N, A, B;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        pizzaA = new int[N+1];
        pizzaB = new int[N+1];
        Arrays.fill(pizzaA,0);
        Arrays.fill(pizzaB,0);
        pizzaA[0]=1;
        pizzaB[0]=1;
        st = new StringTokenizer(br.readLine());
        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        pA = new int[A];
        pB = new int[B];
        int maxPA = 0, maxPB=0;
        for(int i = 0; i<A; i++){
            st = new StringTokenizer(br.readLine());
            pA[i] = Integer.parseInt(st.nextToken());
            maxPA+=pA[i];
        }
        for(int i = 0; i<B; i++){
            st = new StringTokenizer(br.readLine());
            pB[i] = Integer.parseInt(st.nextToken());
            maxPB+=pB[i];
        }
        for(int i = 0;i<A;i++) getPizzaA(i,(i+1)%A,pA[i]);
        for(int i = 0;i<B;i++) getPizzaB(i,(i+1)%B,pB[i]);
        if(maxPA<=N) pizzaA[maxPA]=1;
        if(maxPB<=N) pizzaB[maxPB]=1;
        int ans = 0,l,r;
        for(int i = 0;i<=N;i++){
            l = i;
            r = N-i;
            ans+=pizzaA[l]*pizzaB[r];
        }
        System.out.println(ans);
    }

    public static void getPizzaA(int start, int now, int p){
        if(now==start || p>N) return;
        pizzaA[p]+=1;
        getPizzaA(start,(now+1)%A,p+pA[now]);
    }

    public static void getPizzaB(int start, int now, int p){
        if(now==start || p>N) return;
        pizzaB[p]+=1;
        getPizzaB(start,(now+1)%B,p+pB[now]);
    }
}
