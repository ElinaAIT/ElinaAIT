import java.util.*;

class Student {
    int id;
    String name;
    int age;
    Set<String> courses;

    public Student(int id, String name, int age) {
        this.id = id;
        this.name = name;
        this.age = age;
        this.courses = new HashSet<>();
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public Set<String> getCourses() {
        return courses;
    }

    public void addCourse(String course) {
        courses.add(course);
    }

    public void removeCourse(String course) {
        courses.remove(course);
    }

    public String toString() {
        return "Student{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", age=" + age +
                ", courses=" + courses +
                '}';
    }
}

class StudentManager {
    Map<Integer, Student> students;

    public StudentManager() {
        students = new HashMap<>();
    }

    public void addStudent(int id, String name, int age) {
        students.put(id, new Student(id, name, age));
    }

    public void removeStudent(int id) {
        students.remove(id);
    }

    public void updateStudentDetails(int id, String name, int age, Set<String> courses) {
        Student student = students.get(id);
        if (student != null) {
            student.setName(name);
            student.setAge(age);
            student.getCourses().clear();
            student.getCourses().addAll(courses);
        }
    }

    public void displayAllStudentsSortedById() {
        List<Integer> sortedIds = new ArrayList<>(students.keySet());
        Collections.sort(sortedIds);

        for (int id : sortedIds) {
            System.out.println(students.get(id));
        }
    }

    public void searchStudentById(int id) {
        Student student = students.get(id);
        if (student != null) {
            System.out.println(student);
        } else {
            System.out.println("Student not found with id" + id);
        }
    }

    public void listStudentsByCourse(String course) {
        for (Student student : students.values()) {
            if (student.getCourses().contains(course)) {
                System.out.println(student);
            }
        }
    }
}
    class Main {
        public static void main(String[] args) {
            StudentManager manager = new StudentManager();

            manager.addStudent(1, "Elli", 18);
            manager.addStudent(2, "Guli", 17);
            manager.addStudent(3, "Aiyma", 17);

            manager.updateStudentDetails(1, "Elli", 18, new HashSet<>(Arrays.asList("Mathematics", "PL","Computer Science")));
            manager.updateStudentDetails(2, "Guli", 18, new HashSet<>(Arrays.asList("Computer Science", "Pl","Mathematics")));
            manager.updateStudentDetails(3, "Aiyma", 18, new HashSet<>(Arrays.asList("Computer Science", "Pl","Mathematics")));

            System.out.println("All students sorted by Id:");
            manager.displayAllStudentsSortedById();

            System.out.println("\nSearching for student with Id:");
            manager.searchStudentById(1);
            manager.searchStudentById(2);
            manager.searchStudentById(3);

            System.out.println("\nStudenty By course:");
            manager.listStudentsByCourse("PL");

            manager.removeStudent(1);
            System.out.println("\nAll Students Sorted By Id:");
            manager.displayAllStudentsSortedById();
        }
    }
