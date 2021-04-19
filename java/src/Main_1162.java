import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main_1162 {
    static StringTokenizer st;
    static int N, M, K;
    static ArrayList<Node>[] adj;
    static long[][] dp_arr;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        adj = new ArrayList[N+1];
        for(int i = 0;i<N+1;i++) adj[i] = new ArrayList<Node>();
        dp_arr = new long[21][N+1];
        for (int i = 0; i<21;i++) Arrays.fill(dp_arr[i],Long.MAX_VALUE);
        for (int i = 0 ; i<M;i++){
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());
            adj[n].add(new Node(m,p));
            adj[m].add(new Node(n,p));
        }
        PriorityQueue<Node2> priorityQueue = new PriorityQueue<>();
        priorityQueue.add(new Node2(0,1,K));
        while(!priorityQueue.isEmpty()){
            Node2 node2 = priorityQueue.poll();
            if(node2.now==N){
                System.out.println(node2.p);
                break;
            }
            if(dp_arr[node2.k][node2.now]<node2.p) continue;
            for(int i = 0;i<adj[node2.now].size();i++){
                Node node = adj[node2.now].get(i);
                if(dp_arr[node2.k][node.next]>node2.p+node.p){
                    dp_arr[node2.k][node.next] = node2.p+node.p;
                    priorityQueue.add(new Node2(node2.p+node.p,node.next,node2.k));
                }
                if(node2.k>0 && dp_arr[node2.k-1][node.next]>node2.p){
                    dp_arr[node2.k-1][node.next] = node2.p;
                    priorityQueue.add(new Node2(node2.p,node.next,node2.k-1));
                }
            }
        }
    }

    static class Node2 implements Comparable<Node2>{
        long p;
        int now;
        int k;

        public Node2(long p, int now, int k){
            this.now = now;
            this.p = p;
            this.k = k;
        }

        @Override
        public int compareTo(Node2 node2) {
            return this.p<=node2.p?-1:1;
        }
    }

    static class Node{
        int next;
        int p;
        public Node(int next, int p){
            this.next = next;
            this.p = p;
        }
    }
}
