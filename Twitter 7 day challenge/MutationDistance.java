package co.sachin.google;

import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

public class MutationDistance {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}     
	static int findMutationDistanceance(String start, String end, String[] bank) 
	{
		if(start.equals(end)) 
		{
			return 0;
		}      
		
    
    Set<String> visitedSet = new HashSet<String>();
    Set<String> bankSet = new HashSet<String>(Arrays.asList(bank));
    int distance = 0;
    Queue<String> sequenceQueue = new LinkedList<String>();
    
    sequenceQueue.offer(start);
    visitedSet.add(start);
    Set<Character> charSet = new HashSet<Character>() {{
        add('A');
        add('C');
        add('G');
        add('T');
    }};      
    
    while(!sequenceQueue.isEmpty()) {
        int size = sequenceQueue.size();
        while(size > 0) {
            String curr = sequenceQueue.poll();
            if(curr.equals(end)) {
            	return distance;
            }                
            char[] currArray = curr.toCharArray();
            for(int i = 0; i < currArray.length; i++) {
                char temp = currArray[i];
                for(char c: charSet) {
                    currArray[i] = c;
                    String next = new String(currArray);
                    if(!visitedSet.contains(next) && bankSet.contains(next)) 
                    {
                        visitedSet.add(next);
                        sequenceQueue.offer(next);
                    }
                }
                currArray[i] = temp;
            }
            size--;
        }
        distance++;
    }
    return -1;


}

}
