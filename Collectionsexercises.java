import java.util.*;

public class ArrayListOperations {
    public static void main(String[] args) {
        ArrayList<String> arrayList = new ArrayList<>(Arrays.asList("Apple", "Banana", "Cherry", "Date"));

        // Write a Java program to clone an array list to another array list.
        ArrayList<String> clonedList = new ArrayList<>(arrayList);
        System.out.println("Cloned ArrayList: " + clonedList);

        // Write a Java program to empty an array list.
        arrayList.clear();
        System.out.println("ArrayList after clearing: " + arrayList);

        // Write a Java program to test whether an array list is empty or not.
        System.out.println("Is the array list empty? " + arrayList.isEmpty());

        // Write a Java program for trimming the capacity of an array list.
        ArrayList<Integer> listWithCapacity = new ArrayList<>(100);
        listWithCapacity.trimToSize();
        System.out.println("Trimmed ArrayList capacity: " + listWithCapacity.size());

        // Write a Java program to increase an array list size.
        ArrayList<Integer> expandedList = new ArrayList<>(Arrays.asList(1, 2, 3));
        expandedList.ensureCapacity(10);
        System.out.println("Expanded ArrayList size: " + expandedList.size());

        // Write a Java program to replace the second element of an ArrayList with the specified element.
        arrayList.addAll(Arrays.asList("Apple", "Banana", "Cherry", "Date"));
        arrayList.set(1, "Blueberry");
        System.out.println("ArrayList after replacing second element: " + arrayList);

        // Write a Java program to print all the elements of an ArrayList using the elements' position.
        for (int i = 0; i < arrayList.size(); i++) {
            System.out.println("Element at position " + i + ": " + arrayList.get(import java.util.*;

public class LinkedListOperations {
    public static void main(String[] args) {
        LinkedList<String> linkedList = new LinkedList<>(Arrays.asList("Apple", "Banana", "Cherry", "Date"));

        // Write a Java program to insert some elements at the specified position into a linked list.
        linkedList.add(2, "Blueberry");
        System.out.println("LinkedList after insertion at position 2: " + linkedList);

        // Write a Java program to get the first and last occurrence of the specified elements in a linked list.
        System.out.println("First occurrence of 'Banana': " + linkedList.indexOf("Banana"));
        System.out.println("Last occurrence of 'Banana': " + linkedList.lastIndexOf("Banana"));

        // Write a Java program to display elements and their positions in a linked list.
        for (int i = 0; i < linkedList.size(); i++) {
            System.out.println("Element at position " + i + ": " + linkedList.get(i));
        }

        // Write a Java program to remove a specified element from a linked list.
        linkedList.remove("Cherry");
        System.out.println("LinkedList after removing 'Cherry': " + linkedList);

        // Write a Java program to remove the first and last elements from a linked list.
        linkedList.removeFirst();
        linkedList.removeLast();
        System.out.println("LinkedList after removing first and last elements: " + linkedList);

        // Write a Java program to remove all elements from a linked list.
        linkedList.clear();
        System.out.println("LinkedList after removing all elements: " + import java.util.*;

public class HashSetOperations {
    public static void main(String[] args) {
        HashSet<Integer> hashSet = new HashSet<>(Arrays.asList(1, 3, 5, 7, 9));
        
        // Write a Java program to clone a hash set to another hash set.
        HashSet<Integer> clonedSet = new HashSet<>(hashSet);
        System.out.println("Cloned HashSet: " + clonedSet);

        // Write a Java program to convert a hash set to an array.
        Integer[] array = hashSet.toArray(new Integer[0]);
        System.out.println("HashSet as Array: " + Arrays.toString(array));

        // Write a Java program to convert a hash set to a tree set.
        TreeSet<Integer> treeSet = new TreeSet<>(hashSet);
        System.out.println("HashSet converted to TreeSet: " + treeSet);

        // Write a Java program to find numbers less than 7 in a tree set.
        System.out.println("Numbers less than 7: " + treeSet.headSet(7));

        // Write a Java program to compare two hash set.
        HashSet<Integer> anotherSet = new HashSet<>(Arrays.asList(1, 3, 5, 7, 10));
        System.out.println("HashSets are equal: " + hashSet.equals(anotherSet));

        // Write a Java program to compare two sets and retain elements that are the same.
        hashSet.retainAll(anotherSet);
        System.out.println("Elements retained in both sets: " + hashSet);

        // Write a Java program to remove all elements from a hash set.
        hashSet.clear();
        System.out.println("HashSet after removing all elements: " + import java.util.*;

public class TreeSetOperations {
    public static void main(String[] args) {
        TreeSet<Integer> treeSet = new TreeSet<>(Arrays.asList(1, 3, 5, 7, 9, 11));

        // Write a Java program to get the number of elements in a tree set.
        System.out.println("Number of elements in the TreeSet: " + treeSet.size());

        // Write a Java program to compare two tree sets.
        TreeSet<Integer> anotherTreeSet = new TreeSet<>(Arrays.asList(1, 3, 5, 7, 9));
        System.out.println("Are the two TreeSets equal? " + treeSet.equals(anotherTreeSet));

        // Write a Java program to find numbers less than 7 in a tree set.
        System.out.println("Numbers less than 7 in the TreeSet: " + treeSet.headSet(7));

        // Write a Java program to get the element in a tree set which is greater than or equal to the given element.
        int givenElement = 6;
        System.out.println("Element >= " + givenElement + ": " + treeSet.ceiling(givenElement));

        // Write a Java program to get the element in a tree set less than or equal to the given element.
        System.out.println("Element <= " + givenElement + ": " + treeSet.floor(givenElement));

        // Write a Java program to get the element in a tree set strictly greater than or equal to the given element.
        System.out.println("Element > " + givenElement + ": " + treeSet.higher(givenElement));

        // Write a Java program to get an element in a tree set that has a lower value than the given element.
        System.out.println("Element < " + givenElement + ": " + treeSet.lower(import java.util.*;

public class PriorityQueueOperations {
    public static void main(String[] args) {
        // Create a priority queue with Integer elements
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Arrays.asList(10, 20, 15, 30, 5));

        // Write a Java program to count the number of elements in a priority queue.
        System.out.println("Number of elements in the PriorityQueue: " + priorityQueue.size());

        // Write a Java program to compare two priority queues.
        PriorityQueue<Integer> anotherQueue = new PriorityQueue<>(Arrays.asList(5, 10, 15, 20, 30));
        System.out.println("Are the two PriorityQueues equal? " + priorityQueue.equals(anotherQueue));

        // Write a Java program to retrieve the first element of the priority queue.
        System.out.println("First element in the PriorityQueue: " + priorityQueue.peek());

        // Write a Java program to retrieve and remove the first element.
        System.out.println("Retrieved and removed first element: " + priorityQueue.poll());
        System.out.println("PriorityQueue after removal: " + priorityQueue);

        // Write a Java program to convert a priority queue to an array containing all its elements.
        Object[] array = priorityQueue.toArray();
        System.out.println("PriorityQueue as Array: " + Arrays.toString(array));

        // Write a Java program to convert a Priority Queue element to string representations.
        String priorityQueueString = priorityQueue.toString();
        System.out.println("String representation of PriorityQueue: " + priorityQueueString);

        // Write a Java program to change priorityQueue to maximum priority queue.
        PriorityQueue<Integer> maxPriorityQueue = new PriorityQueue<>(Collections.reverseOrder());
        maxPriorityQueue.addAll(priorityQueue);
        System.out.println("Max PriorityQueue: " + import java.util.*;

public class HashMapOperations {
    public static void main(String[] args) {
        // Create a sample HashMap
        HashMap<String, Integer> map = new HashMap<>();
        map.put("Apple", 3);
        map.put("Banana", 2);
        map.put("Cherry", 5);

        // Write a Java program to copy all mappings from the specified map to another map.
        HashMap<String, Integer> copiedMap = new HashMap<>(map);
        System.out.println("Copied HashMap: " + copiedMap);

        // Write a Java program to remove all mappings from a map.
        map.clear();
        System.out.println("HashMap after clearing all mappings: " + map);

        // Write a Java program to check whether a map contains key-value mappings (empty) or not.
        System.out.println("Is the map empty? " + map.isEmpty());

        // Write a Java program to get a shallow copy of a HashMap instance.
        HashMap<String, Integer> shallowCopy = new HashMap<>(map);
        System.out.println("Shallow copy of HashMap: " + shallowCopy);

        // Write a Java program to test if a map contains a mapping for the specified key.
        System.out.println("Does the map contain the key 'Apple'? " + copiedMap.containsKey("Apple"));

        // Write a Java program to test if a map contains a mapping for the specified value.
        System.out.println("Does the map contain the value '5'? " + copiedMap.containsValue(5));

        // Write a Java program to create a set view of the mappings contained in a map.
        Set<Map.Entry<String, Integer>> entrySet = copiedMap.entrySet();
        System.out.println("Set view of the mappings in the HashMap: " + entrySet);
    }
}
}


