import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main_14427 {
    static StringTokenizer st;
    static int N, size;
    static int[] tree;
    static int[] arr;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        size = 1;
        while (size<=N){
            size<<=1;
        }
        tree = new int[size*2];
        Arrays.fill(tree,-1);
        arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for(int i = 0 ; i<N;i++){
            arr[i] = Integer.parseInt(st.nextToken());
            tree[size+i]=i;
        }
        int ed = size;
        while(ed>1){
            int start = ed>>1;
            for(int i = start; i<ed;i++){
                int l = tree[i<<1], r = tree[i<<1|1];
                if(l==-1) break;
                if(r==-1 || arr[l]<=arr[r]) tree[i] = l;
                else tree[i]=r;
            }
            ed=start;
        }
        st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        for(int i = 0; i<M;i++){
            String[] input = br.readLine().strip().split(" ");
            if(input.length==1) System.out.println(tree[1]+1);
            else update(Integer.parseInt(input[1])-1,Integer.parseInt(input[2]));
        }
    }

    static void update(int idx, int v){
        arr[idx] = v;
        int start = (size+idx)>>1;
        while(start>0){
            int l = tree[start<<1], r = tree[start<<1|1];
            if(r==-1 || arr[l]<=arr[r]) tree[start] = l;
            else tree[start] = r;
            start>>=1;
        }
    }
}
