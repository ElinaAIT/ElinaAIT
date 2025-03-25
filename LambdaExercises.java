import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.BiFunction;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;
@FunctionalInterface
interface MathOperation {
    //Task 1
    int operate(int i,int g);
}

class main {
    public static void main(String[] args) {
        MathOperation addition = (i, g) -> i + g;
        MathOperation subraction = (i, g) -> i - g;
        MathOperation multiplication = (i, g) -> i * g;
        MathOperation division = (i, g) -> i / g;


        System.out.println("Addition:" + addition.operate(7, 3));
        System.out.println("Subraction:" + subraction.operate(13, 3));
        System.out.println("Multiplication:" + multiplication.operate(10, 3));
        System.out.println("Devision" + division.operate(30, 10));


        //Task 2
        List<Integer> numbers = Arrays.asList(10, 15, 22, 33, 40, 55);

        Predicate<Integer> isOdd = num -> num % 2 != 0;

        System.out.print("Odd Numbers: ");
        for (Integer num : numbers) {
            if (isOdd.test(num)) { // Используем Predicate для проверки
                System.out.print(num + " ");
            }

        //Task 3
            List<String> names = Arrays.asList("Guli", "Aiyma", "Elli", "Isla","Adina","Sumaya","Bermet","Tima","Nur","Aya");

            names.sort((a, b) -> b.compareTo(a));

            System.out.println("Sorted Names: " + names);
            

         //Task 4
            List<String> words = Arrays.asList("hello", "java", "lambda");
            Function<String, String> transform = str ->
                    new StringBuilder(str.toUpperCase()).reverse().toString();

            List<String> transformedWords = new ArrayList<>();
            for (String word : words) {
                transformedWords.add(transform.apply(word));
            }

            System.out.println("Transformed Strings: " + transformedWords);


          //Task 5
            List<String> cities = Arrays.asList("New York", "London", "Tokyo", "Berlin");

            Consumer<String> printCity = city -> System.out.println(city);

            cities.forEach(printCity);
            
            
            
          //Task 6
            cities.forEach(System.out::println);
            
            
            
          //Task 7
            int a = 100, b = 70;

            BiFunction<Integer, Integer, Integer> max = (x, y) -> x > y ? x : y;

            BiFunction<Integer, Integer, Integer> min = (x, y) -> x < y ? x : y;

            int maxNumber = max.apply(a, b);
            int minNumber = min.apply(a, b);

            System.out.println("Max: " + maxNumber);
            System.out.println("Min: " + minNumber);
            
        }
    }
}
