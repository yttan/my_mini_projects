
import java.io.*;
import java.util.*;
public class Johnsons {

    private static int INF = Integer.MAX_VALUE;


    private int edgenumber;
    private int vexnumber;
    private int addededgenumber;
    private int addedvexnumber;


    
    private class VexObj {
        String data;          
        EdgeObj firstEdge;   
    };

    private class EdgeObj {
        int weight;
        int position;
        EdgeObj nextEdge;       
    }

    private  VexObj[] vertexes;
    private  VexObj[] addedvertexes;
   
   
    private int getpos(String indata) {
        for(int m=0; m<vexnumber; m++){
            char x;
            char y;
            x=vertexes[m].data.charAt(0);
            y=indata.charAt(0);
            if(x==y){
                return m;
            }
        }
        return -1;
    }

    private int getaddedpos(String indata) {
        for(int m=0; m<addedvexnumber; m++){
            char x;
            x=addedvertexes[m].data.charAt(0);
            char y;
            y=indata.charAt(0);
            if(x==y){
                return m;
            }
        }
        return -1;
    }

    private void link(EdgeObj nodelist,EdgeObj node ) {
        EdgeObj temp = nodelist;
        while(temp.nextEdge!=null)
            temp = temp.nextEdge;
        temp.nextEdge = node;
    }

 
    
    public Johnsons(String[] vexs, String[][] edges,String[] addedvexs, String[][] addededges) {



        addedvexnumber = addedvexs.length;
        addededgenumber = addededges.length;
        vexnumber=vexs.length;
        edgenumber=edges.length;


        addedvertexes = new VexObj[addedvexnumber];
        for (int i = 0; i < addedvexnumber; i++) {
            addedvertexes[i] = new VexObj();
            addedvertexes[i].data = addedvexs[i];
            addedvertexes[i].firstEdge = null;
        }
        for (int i = 0; i < addededgenumber; i++) {
            String point1 = addededges[i][0];
            String point2 = addededges[i][1];
            int weight = Integer.parseInt(addededges[i][2]);

            int position1 = getaddedpos(point1);
            int position2 = getaddedpos(point2);
            


            EdgeObj temppoint = new EdgeObj();
            temppoint.position = position2;
            temppoint.weight = weight;

          
            if(addedvertexes[position1].firstEdge == null)
              addedvertexes[position1].firstEdge = temppoint;
            else
                link(addedvertexes[position1].firstEdge, temppoint);

        }


        int[] dist = new int[addedvexnumber];

        for(int v=0;v<addedvexnumber;v++){
            dist[v]=0;
        }

        for(int i = 0; i < (addedvexnumber - 1); i++){
            for (int e = 0; e < addededgenumber; e++) {
                String point1 = addededges[e][0];
                String point2 = addededges[e][1];
                int weight = Integer.parseInt(addededges[e][2]);
                int position1 = getaddedpos(point1);
                int position2 = getaddedpos(point2);           
                if(dist[position2] > dist[position1] + weight){
                    dist[position2] = dist[position1] + weight;
                }
            }
        }
    
        vexnumber = vexs.length;
        edgenumber = edges.length;
        
        vertexes = new VexObj[vexnumber];
        for (int i = 0; i < vexnumber; i++) {
            vertexes[i] = new VexObj();
            vertexes[i].data = vexs[i];
            vertexes[i].firstEdge = null;
        }
        for (int i = 0; i < edgenumber; i++) {
            String point1 = edges[i][0];
            String point2 = edges[i][1];
            int position1 = getpos(point1);
            int position2 = getpos(point2);
            int weight = Integer.parseInt(edges[i][2]);
            
            EdgeObj temppoint = new EdgeObj();
            temppoint.position = position2;
            temppoint.weight = weight+dist[(position1+1)]-dist[(position2+1)];
          
            if(vertexes[position1].firstEdge == null)
              vertexes[position1].firstEdge = temppoint;
            else
                link(vertexes[position1].firstEdge, temppoint);
        }

        int[] h = new int[vexnumber];
        for(int i=0;i<vexnumber;i++){
            h[i]=dist[i+1];
        }

        int[] myprev = new int[vexnumber];
        int[] mydist = new int[vexnumber]; 
              System.out.print("  ");
        for(int i =0; i< vexnumber;i++){


            System.out.print(vertexes[i].data);

            System.out.print(" ");
            
        }
          System.out.println(" ");
        
        for(int i =0; i< vexnumber;i++){
            System.out.print(vertexes[i].data);

            System.out.print(" ");
            dijkstra(i, myprev, mydist,h);

        }
        


    }

    private int getWeight(int start, int end) {
        if (start==end)
            return 0;
        EdgeObj node = vertexes[start].firstEdge;
        while (node!=null) {
            if (end==node.position)
                return node.weight;
            node = node.nextEdge;
        }
        return INF;
    }
    
    public void dijkstra(int startindex, int[] prev, int[] dist, int[] h) {
        boolean[] flag = new boolean[vexnumber];
        int[] result = new int[vexnumber];

        for (int i = 0; i < vexnumber; i++) {
            flag[i] = false;            
            prev[i] = -1;                
            dist[i] = getWeight(startindex, i);
        }
        

        flag[startindex] = true;
        dist[startindex] = 0;
        
        int k = 0;
        for (int i = 1; i < vexnumber; i++) {
            int min = INF;
            for (int j = 0; j < vexnumber; j++) {
                if (flag[j]==false && dist[j]<min) {
                    min = dist[j];
                    k = j;
                }
            }
            flag[k] = true;
            for (int j = 0; j < vexnumber; j++) {
                int tmp = getWeight(k, j);
                tmp = (tmp==INF ? INF : (min + tmp)); 
                if (flag[j]==false && (tmp<dist[j]) )
                {
                    dist[j] = tmp;
                    prev[j] = k;
                }
            }
            
        }
    
        for(int i=0;i<vexnumber;i++){
            result[i]=dist[i]+h[i]-h[startindex];
        } 
        int p= INF/2;
        int np = -INF/2;
    
        for (int i = 0;i < vexnumber;i++){
            if(result[i]< p && result[i] > np){
                System.out.print(result[i]);
            }
            
            else{
                System.out.print("!");
            }

            System.out.print(" ");
        }

        System.out.println(" ");


    }




    public static void main(String[] args) {
        String fileName = "johnsonsGraphData.txt";
        String line = null;   
        int row = 0 ;
        List<String> column1 = new ArrayList<String>();
        List<String> column2 = new ArrayList<String>();
        List<String> column3 = new ArrayList<String>();        
        try {
            FileReader fileReader = new FileReader(fileName);
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            while((line = bufferedReader.readLine()) != null) {
                String[] templine = line.split(" ");
                column1.add(templine[0]);
                column2.add(templine[1]);
                column3.add(templine[2]);
                row ++ ;
            }
            bufferedReader.close();
        }
        catch(FileNotFoundException ex) {
            System.out.println("Unable to open file '" + fileName );                
        }
        catch(IOException ex) {
            System.out.println("Error reading file '" + fileName );          
        }
        List<String> vexlist = new ArrayList<String>();
        List<String> addedvexlist = new ArrayList<String>();
  
        for (int k=0; k<row; k++) {  
            if(!vexlist.contains(column1.get(k))) {  
                vexlist.add(column1.get(k));  
            }  
            if(!vexlist.contains(column2.get(k))) {  
                vexlist.add(column2.get(k));
            }
        }

        addedvexlist.add("0");
        for (int k=0; k<row; k++) {  
            if(!addedvexlist.contains(column1.get(k))) {  
                addedvexlist.add(column1.get(k));  
            }  
            if(!addedvexlist.contains(column2.get(k))) {  
                addedvexlist.add(column2.get(k));
            }
        }

        int vexnum = vexlist.size();
        int addedvexnum= addedvexlist.size();

        String[] vexs = new String[vexnum];
         for(int i=0;i<vexnum;i++){
            vexs[i]=vexlist.get(i);
        }//

        String[] addedvexs = new String[addedvexnum];
         for(int i=0;i<addedvexnum;i++){
            addedvexs[i]=addedvexlist.get(i);
        }//

        String[][] edges= new String[row][3];        
        for(int i=0;i<row;i++){
            edges[i][0]=column1.get(i);
            edges[i][1]=column2.get(i);
            edges[i][2]=column3.get(i);
        }//

        int row2 = row + vexnum;
        String[][] addededges= new String[row2][3];        
        for(int i=0;i<row;i++){
            addededges[i][0]=column1.get(i);
            addededges[i][1]=column2.get(i);
            addededges[i][2]=column3.get(i);
        }
        for(int i=row;i<row2;i++){
            addededges[i][0]="0";
            addededges[i][1]=vexs[(i-row)];
            addededges[i][2]="0";
        }
        
        Johnsons myG;
        myG = new Johnsons(vexs,edges,addedvexs,addededges);

        
    }
}
