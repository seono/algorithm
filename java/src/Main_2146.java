import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main_2146 {
    static StringTokenizer st;
    static int[][] arr;
    static int N;
    static int eCnt = 1;
    static int[] dy = {0,0,-1,1};
    static int[] dx = {1,-1,0,0};
    static boolean[][] visited;
    static int ans = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N][N];
        for(int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N;j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        visited = new boolean[N][N];
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N;j++){
                if(arr[i][j]==1){
                    eCnt+=1;
                    arr[i][j]=eCnt;
                    bfs(i,j);
                }
            }
        }
        while (true){
            visited = new boolean[N][N];
            for(int i = 0; i < N; i++){
                for(int j = 0; j < N;j++){
                    if(visited[i][j] || arr[i][j]==0) continue;
                    int tmp = bfs2(i,j);
                    if(tmp>0){
                        System.out.println(tmp);
                        return;
                    }
                }
            }
            ans+=1;
        }
    }
    static void print(){
        for(int i = 0;i<N;i++){
            System.out.println(Arrays.toString(arr[i]));
        }
        System.out.println();
    }

    static int bfs2(int y, int x){
        int earthNum = arr[y][x];
        List<Node> nodeList = new ArrayList<>(Collections.singletonList(new Node(y,x)));
        visited[y][x]=true;
        int ret = 0;
        while (nodeList.size()>0){
            Node node = nodeList.get(0);
            nodeList.remove(0);
            for(int k = 0 ; k<4;k++){
                int ny = node.y+dy[k], nx = node.x+dx[k];
                if(ny<0 || ny>=N || nx<0 || nx>=N) continue;
                if(arr[ny][nx]==0){
                    arr[ny][nx]=earthNum;
                    visited[ny][nx]=true;
                    continue;
                }else if (arr[ny][nx]!=earthNum){
                    if(visited[ny][nx]) ret = ans<<1|1;
                    else return ans<<1;
                }
                if(visited[ny][nx])continue;
                visited[ny][nx]=true;
                nodeList.add(new Node(ny,nx));
            }
        }
        return ret;
    }

    static void bfs(int y, int x){
        List<Node> nodeList = new ArrayList<>(Collections.singletonList(new Node(y,x)));
        visited[y][x]=true;
        while(nodeList.size()>0){
            Node node = nodeList.get(0);
            nodeList.remove(0);
            for(int k = 0 ; k<4;k++){
                int ny = node.y+dy[k], nx = node.x+dx[k];
                if(ny<0 || ny>=N || nx<0 || nx>=N || visited[ny][nx]) continue;
                if(arr[ny][nx]==0) continue;
                visited[ny][nx]=true;
                arr[ny][nx]=eCnt;
                nodeList.add(new Node(ny,nx));
            }
        }
    }

    static class Node{
        int x;
        int y;

        public Node(int y, int x){
            this.y = y;
            this.x = x;
        }
    }
}
