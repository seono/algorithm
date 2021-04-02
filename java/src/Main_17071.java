import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main_17071 {
    static StringTokenizer st;
    static int N, K;
    static int ans = 0;
    static boolean[][] visited = new boolean[2][500001];
    static Queue<Integer> queue;
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        for(int i = 0 ; i<2;i++) Arrays.fill(visited[i],false);
        queue = new LinkedList<>();
        queue.add(N);
        System.out.println(sol());
    }


    static int sol(){
        if(N==K) return 0;
        int ret = 1;
        while(queue.size()>0){
            int size = queue.size();
            K+=ret;
            if (K>500000) return -1;
            if(visited[ret%2][K]) return ret;
            while (size>0){
                size-=1;
                int tmp = queue.poll();
                if(tmp+1==K || tmp-1 == K || tmp<<1 == K) return ret;
                if(tmp+1<=500000 && !visited[ret%2][tmp+1]){
                    visited[ret%2][tmp+1] = true;
                    queue.add(tmp+1);
                }
                if(tmp-1>0 && !visited[ret%2][tmp-1]){
                    visited[ret%2][tmp-1] = true;
                    queue.add(tmp-1);
                }
                if(tmp<<1 <= 500000 && !visited[ret%2][tmp<<1]){
                    visited[ret%2][tmp<<1] = true;
                    queue.add(tmp<<1);
                }
            }
            ret+=1;
        }
        return -1;
    }

}
