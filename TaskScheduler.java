import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.*;
import java.util.HashMap;
import java.util.Map;

//1 задание
class MergeLists {

    public static <T> List<T> mergeLists(List<T> list1, List<T> list2) {
        List<T> mergedList = new ArrayList<>();
        int maxSize = Math.max(list1.size(), list2.size());

        for (int i = 0; i < maxSize; i++) {
            if (i < list1.size()) {
                mergedList.add(list1.get(i));
            }
            if (i < list2.size()) {
                mergedList.add(list2.get(i));
            }
        }

        return mergedList;
    }

    public static void main(String[] args) {
        List<Integer> list1 = Arrays.asList(1, 3, 5);
        List<Integer> list2 = Arrays.asList(2, 4, 6, 8, 10);

        List<Integer> mergedList = mergeLists(list1, list2);

        System.out.println("Объединённый список: " + mergedList);
    }
}


//2 задание
class PrintMap {

    public static <K, V> void printMap(Map<K, V> map) {
        for (Map.Entry<K, V> entry : map.entrySet()) {
            System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
        }
    }

    public static void main(String[] args) {
        Map<String, Integer> map = new HashMap<>();
        map.put("One", 1);
        map.put("Two", 2);
        map.put("Three", 3);

        printMap(map);
    }
}


class Task implements Comparable<Task> {
    String taskName;
    int priority;
    int duration;

    public Task(String taskName, int priority, int duration) {
        this.taskName = taskName;
        this.priority = priority;
        this.duration = duration;
    }

    @Override
    public int compareTo(Task other) {
        if (this.priority == other.priority) {
            return Integer.compare(this.duration, other.duration);
        }
        return Integer.compare(other.priority, this.priority);
    }

    @Override
    public String toString() {
        return "[priority " + priority + "] " + taskName + " (duration: " + duration + " mins)";
    }
}

public class TaskScheduler {
    private PriorityQueue<Task> taskQueue = new PriorityQueue<>();
    private Queue<Task> pendingTasks = new LinkedList<>();

    public void addTask(String name, int priority, int duration) {
        Task task = new Task(name, priority, duration);
        taskQueue.offer(task);
        System.out.println("Task Added: " + task);
    }

    public void processNextTask() {
        if (!taskQueue.isEmpty()) {
            Task task = taskQueue.poll();
            System.out.println("Processing Task: " + task);
        } else if (!pendingTasks.isEmpty()) {
            Task task = pendingTasks.poll();
            System.out.println("Processing Pending Task: " + task);
        } else {
            System.out.println("No tasks to process.");
        }
    }

    public void delayTask(String name) {
        Iterator<Task> iterator = taskQueue.iterator();
        while (iterator.hasNext()) {
            Task task = iterator.next();
            if (task.taskName.equals(name)) {
                iterator.remove();
                pendingTasks.offer(task);
                System.out.println("Delaying Task: " + task);
                return;
            }
        }
        System.out.println("Task not found for delay.");
    }

    public void showScheduledTasks() {
        System.out.println("Scheduled Tasks (sorted by priority):");

        PriorityQueue<Task> tempQueue = new PriorityQueue<>(taskQueue);
        while (!tempQueue.isEmpty()) {
            System.out.println(tempQueue.poll());
        }
    }

    public void showPendingTasks() {
        System.out.println("Pending Tasks (FIFO Order):");
        for (Task task : pendingTasks) {
            System.out.println(task);
        }
    }

    public static void main(String[] args) {
        TaskScheduler scheduler = new TaskScheduler();

        scheduler.addTask("Bug Fixing", 7, 25);
        scheduler.addTask("System Update", 9, 45);
        scheduler.addTask("Database Backup", 1, 30);
        scheduler.addTask("Code Review", 3, 20);
        scheduler.addTask("Deploy New Feature", 7, 50);

        scheduler.showScheduledTasks();
        scheduler.processNextTask();
        scheduler.delayTask("Code Review");
        scheduler.showScheduledTasks();
        scheduler.processNextTask();
        scheduler.showPendingTasks();
        scheduler.processNextTask();
        scheduler.processNextTask();
        scheduler.processNextTask();
        scheduler.showScheduledTasks();
        scheduler.showPendingTasks();
    }
}
