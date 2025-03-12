public class Book{
    String title;
    String author;
    int yearPublished;

    public Book(String title,String author,int yearPublished){
        this.title=title;
        this.author=author;
        this.yearPublished=yearPublished;
    }
    public String getBookInfo(){
        return "Title:" + title + "\nAuthor:" + author + "\nYearOfTheBook:" + yearPublished;
    }
    public void printBookDetails(){
        System.out.println("Title:" + title + "\nAuthor:" + author + "\nYearOfTheBook:" + yearPublished);
    }
}
    class PrintedBook extends Book {
        int numberOfPages;
        String publisher;
        int price;
        public PrintedBook(String title,String author,int yearPublished, int numberOfPages,String publisher) {
            super(title, author, yearPublished);
            this.numberOfPages = numberOfPages;
            this.publisher=publisher;
            this.price = numberOfPages * 3;
        }
        @Override
        public String getBookInfo(){
            return "Title:" + title + "\nAuthor:" + author + "\nYearPublisher:" + yearPublished + "\nNumberofPages:" + numberOfPages + "\nPublisher:" + publisher;
        }

        @Override
        public void printBookDetails(){
            System.out.println("\nTitle:" + title + "\nAuthor:" + author + "\nYearPublisher:" + yearPublished + "\nNumberofPages:" + numberOfPages + "\nPublisher:" + publisher);
        }
        public void bookType(){
            System.out.println("this is a printed book");
        }
    }

    class Ebook extends Book {
        double fileSizeMb;
        String fileFormat;
        double price;
        public Ebook(String title,String author,int yearPublished,double fileSizeMb,String fileFormat){
            super(title,author,yearPublished);
            this.fileSizeMb=fileSizeMb;
            this.fileFormat=fileFormat;
            this.price=fileSizeMb*300;
        }

        @Override
        public String getBookInfo(){
            return "Title:" + title + "\nAuthor:" + author + "\nYearPublisher:" + yearPublished + "\nFileSizeMB:" + fileSizeMb + "\nFileFormat:" + fileFormat;
        }

        @Override
        public void printBookDetails(){
            System.out.println("Title:" + title + "\nAuthor:" + author + "\nYearPublisher:" + yearPublished + "\nFileSizeMB:" + fileSizeMb + "\nFileFormat:" + fileFormat);
        }

        public void bookType() {
            System.out.println("This is a Ebook");
        }
    }
    class mainnnn{
        public static void main(String[] args) {
            PrintedBook printedBook = new PrintedBook("Harry Potter ", "J.K. Rowling", 1997, 223 , "Bloomsbury");
            Ebook eBook = new Ebook("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1999,  0.9 , "PDF");

            System.out.println("Printed Book:");
            printedBook.printBookDetails();
            printedBook.bookType();
            System.out.println("\nEBook:");
            eBook.printBookDetails();
            eBook.bookType();
        }
    }
