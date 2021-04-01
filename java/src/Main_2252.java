import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main_2252 {
    static int N, M;
    static StringTokenizer st;
    static int[] indegree;

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int A,B;
        indegree = new int[N+1];
        List<Integer>[] adj = new ArrayList[N+1];
        Queue<Integer> ans = new LinkedList<>();
        for(int i = 0; i<N+1;i++)
            adj[i] = new ArrayList<>();
        Arrays.fill(indegree,0);
        for(int i = 0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            A = Integer.parseInt(st.nextToken());
            B = Integer.parseInt(st.nextToken());
            indegree[B]+=1;
            adj[A].add(B);
        }
        for(int i = 1; i<=N; i++){
            if(indegree[i]==0){
                ans.add(i);
            }
        }
        StringBuilder sb = new StringBuilder();
        while(ans.size()>0){
            Integer n = ans.poll();
            sb.append(n).append(" ");
            adj[n].forEach(nx->{
                indegree[nx]-=1;
                if(indegree[nx]==0){
                    ans.add(nx);
                }
            });
        }
        System.out.println(sb);
    }
}
