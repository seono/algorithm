import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main_16933 {
    static StringTokenizer st;
    static int N, M, K;
    static int[][] arr;
    static int[] dy = {0,0,-1,1};
    static int[] dx = {1,-1,0,0};
    static int[][] visited;
    static int maxQ = 100000000;

    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        arr = new int[N][M];
        visited = new int[N][M];
        for(int i =0;i<N;i++){
            String[] tmp = br.readLine().strip().split("");
            Arrays.fill(visited[i],Integer.MAX_VALUE);
            for(int j = 0;j<M;j++){
                arr[i][j]=Integer.parseInt(tmp[j]);
            }
        }
        System.out.println(sol());
    }

    static int sol(){
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(1,0,0,0));
        visited[0][0]=0;
        while(queue.size()>0){
            Node node = queue.poll();
            if(node.y==N-1 && node.x==M-1) {
                return node.p;
            }
            for(int i = 0; i<4;i++){
                int ny = node.y + dy[i], nx = node.x+dx[i];
                if(nx<0 || nx>=M || ny<0 || ny>=N || visited[ny][nx]<=node.k) continue;
                if(arr[ny][nx]==1){
                    if(node.k>=K || visited[ny][nx]<=node.k+1) continue;
                    if(node.p%2==1){
                        queue.add(new Node(node.p+1,ny,nx,node.k+1));
                        visited[ny][nx]=node.k+1;
                    }else{
                        queue.add(new Node(node.p+1,node.y,node.x,node.k));
                    }
                }else{
                    queue.add(new Node(node.p+1, ny,nx, node.k));
                    visited[ny][nx]=node.k;
                }
            }
        }
        return -1;
    }


    static class Node{
        int p;
        int y;
        int x;
        int k;

        public Node(int p, int y, int x, int k){
            this.p = p;
            this.y = y;
            this.x = x;
            this.k = k;
        }
    }
}
