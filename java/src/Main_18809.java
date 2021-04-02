import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;

public class Main_18809 {
    static StringTokenizer st;
    static int N, M, G, R;
    static int[][] arr, visited;
    static Queue<Node> queue;
    static int[] dy = {0,0,-1,1};
    static int[] dx = {-1,1,0,0};
    static ArrayList<Node> target, tmp;
    static int ans=0;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        G = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        arr = new int[N][M];
        visited = new int[N][M];
        target = new ArrayList<>();
        for(int i = 0;  i<N;i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0 ; j< M;j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
                if(arr[i][j]==2) target.add(new Node(i,j));
            }
        }
        sol(0,R,G);
        System.out.println(ans);
    }
    static void sol(int idx, int red, int green){
        if(red+green==0) {
            for (int i = 0; i<N;i++){
                if (M >= 0) System.arraycopy(arr[i], 0, visited[i], 0, M);
            }
            ans = Math.max(ans,bfs());
            return;
        }
        if(idx<target.size()){
            if(red>0){
                Node node = target.get(idx);
                arr[node.y][node.x]=3;
                sol(idx+1,red-1,green);
                arr[node.y][node.x]=2;
            }
            if(green>0){
                Node node = target.get(idx);
                arr[node.y][node.x]=4;
                sol(idx+1,red,green-1);
                arr[node.y][node.x]=2;
            }
            sol(idx+1,red,green);
        }
    }

    //visited에 배양액 뿌린 곳 표시 후, queue에 넣어서 시작
    static int bfs(){
        int ret = 0;
        queue = new LinkedList<>();
        boolean[][] check = new boolean[N][M];
        for(int i = 0; i<N;i++) for(int j = 0;j<M;j++) if(visited[i][j]>2) queue.add(new Node(i,j));
        while (!queue.isEmpty()) {
            tmp = new ArrayList<>();
            int size = queue.size();
            while(size>0){
                size--;
                Node node = queue.poll();
                int y = node.y, x = node.x;
                for (int i = 0; i < 4; i++) {
                    int ny = y + dy[i], nx = x + dx[i];
                    if (ny < 0 || ny >= N || nx < 0 || nx >= M) continue;
                    if (visited[y][x]==3 || visited[y][x]==5) {
                        if(visited[ny][nx]==6 && !check[ny][nx]){
                            visited[ny][nx]=7;
                            ret++;
                        }else if(visited[ny][nx]==2||visited[ny][nx]==1){
                            visited[ny][nx]=5;
                            queue.add(new Node(ny,nx));
                            tmp.add(new Node(ny,nx));
                        }
                    }else if(visited[y][x]==4 || visited[y][x]==6){
                        if(visited[ny][nx]==5 && !check[ny][nx]){
                            visited[ny][nx]=7;
                            ret++;
                        }else if(visited[ny][nx]==2||visited[ny][nx]==1){
                            visited[ny][nx]=6;
                            queue.add(new Node(ny,nx));
                            tmp.add(new Node(ny,nx));
                        }
                    }
                }
            }
            tmp.forEach(node -> {
                check[node.y][node.x]=true;
            });
        }
        return ret;
    }

    static class Node{
        int y;
        int x;
        public Node(int y, int x){
            this.y = y;
            this.x = x;
        }

        @Override
        public String toString() {
            return "Node{" +
                    "y=" + y +
                    ", x=" + x +
                    '}';
        }
    }
}
