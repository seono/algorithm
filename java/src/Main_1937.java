import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_1937 {

    static StringTokenizer st;
    static int[][] arr;
    static int[][] dp_arr;
    static int N;
    static int[][] d = {{1,0},{0,1},{-1,0},{0,-1}};
    
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N][N];
        dp_arr = new int[N][N];

        for(int i = 0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j<N; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
                dp_arr[i][j]=-1;
            }
        }
        int ans = 0;
        for(int i = 0; i<N;i++){
            for(int j = 0; j<N;j++) {
                ans = Math.max(ans,dp(i,j)+1);
            }
        }
        System.out.println(ans);
    }

    static int dp(int y, int x){
        if(dp_arr[y][x]!=-1) return dp_arr[y][x];
        int ret = 0;
        for(int i= 0; i<4;i++){
            int ny = y+d[i][0], nx = x+d[i][1];
            if(ny<0 || ny>=N || nx<0 || nx>=N) continue;
            if(arr[ny][nx]>arr[y][x]) ret = Math.max(ret,dp(ny,nx)+1);
        }
        dp_arr[y][x]=ret;
        return ret;
    }
}
