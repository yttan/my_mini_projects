
import java.io.*;
import java.util.*;
public class Topological {

    private class ENode {
        int ivex;       
        ENode nextEdge; 
    }

    private class VNode {
        char data;          
        ENode firstEdge;   
    };

    private List<VNode> mVexs;  


    public Topological(char[] vexs, char[][] edges) {
        
        int vlen = vexs.length;
        int elen = edges.length;

        mVexs = new ArrayList<VNode>();
        for (int i = 0; i < vlen; i++) {
            VNode vnode = new VNode();
            vnode.data = vexs[i];
            vnode.firstEdge = null;
            mVexs.add(vnode);
        }


        for (int i = 0; i < elen; i++) {
 
            char c1 = edges[i][0];
            char c2 = edges[i][1];
      
            int p1 = getPosition(edges[i][0]);
            int p2 = getPosition(edges[i][1]);

            ENode node1 = new ENode();
            node1.ivex = p2;

            if(mVexs.get(p1).firstEdge == null)
                mVexs.get(p1).firstEdge = node1;
            else
                linkLast(mVexs.get(p1).firstEdge, node1);
        }
    }

    private void linkLast(ENode list, ENode node) {
        ENode p = list;

        while(p.nextEdge!=null)
            p = p.nextEdge;
        p.nextEdge = node;
    }

    private int getPosition(char ch) {
        for(int i=0; i<mVexs.size(); i++)
            if(mVexs.get(i).data==ch)
                return i;
        return -1;
    }

    public int topologicalSort() {
        int index = 0;
        int num = mVexs.size();
        int[] ins;               
        char[] tops;           
        Queue<Integer> queue;    

        ins   = new int[num];
        tops  = new char[num];
        queue = new LinkedList<Integer>();


        for(int i = 0; i < num; i++) {

            ENode node = mVexs.get(i).firstEdge;
            while (node != null) {
                ins[node.ivex]++;
                node = node.nextEdge;
            }
        }

   
        for(int i = 0; i < num; i ++)
            if(ins[i] == 0)
                queue.offer(i);                 

        while (!queue.isEmpty()) {              
            int j = queue.poll().intValue();    
            tops[index++] = mVexs.get(j).data;  
            ENode node = mVexs.get(j).firstEdge;

            
            while(node != null) {
                
                ins[node.ivex]--;
                
                if( ins[node.ivex] == 0)
                    queue.offer(node.ivex);    

                node = node.nextEdge;
            }
        }

        if(index != num) {
            System.out.printf("Graph has a cycle\n");
            return 1;
        }


        System.out.printf("== TopSort: ");
        for(int i = 0; i < num; i ++)
            System.out.printf("%c ", tops[i]);
        System.out.printf("\n");

        return 0;
    }

    public static void main(String[] args) {
        String fileName = "graphdata.txt";
        String line = null;   
        int row = 0 ;
        List<Character> list1 = new ArrayList<Character>();
        List<Character> list2 = new ArrayList<Character>();
        try {
            FileReader fileReader = new FileReader(fileName);
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            while((line = bufferedReader.readLine()) != null) {
                list1.add(line.charAt(0));
                list2.add(line.charAt(2));
                row ++ ;
        }
            bufferedReader.close();
        }
        catch(FileNotFoundException ex) {
            System.out.println("Unable to open file '" + fileName + "'");                
        }
        catch(IOException ex) {
            System.out.println("Error reading file '" + fileName + "'");          
        }
        char[][] edges= new char[row][2];
        for(int i=0;i<row;i++){
            edges[i][0]=list1.get(i);
            edges[i][1]=list2.get(i);
        }
        List<Character> list = new ArrayList<Character>();  
        for (int k=0; k<row; k++) {  
            if(!list.contains(list1.get(k))) {  
                list.add(list1.get(k));  
            }  
            if(!list.contains(list2.get(k))) {  
                list.add(list2.get(k));  
            }
        }  
        int num = list.size();
        char[] vexs = new char[num];
         for(int i=0;i<num;i++){
            vexs[i]=list.get(i);
        }

        for(int i=0;i<num;i++){
            System.out.println(vexs[i]);

        }
        for(int i=0;i<row;i++){
            System.out.print(edges[i][0]);
            System.out.println(edges[i][1]);
            
        }
        Topological pG;
        pG = new Topological(vexs, edges);
        pG.topologicalSort();     
    }
}
