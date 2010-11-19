// HelloWorld.java
public class SystemProps {
    public static void main(String[] args) {
        System.out.println("Hello, Java.");

        String property_foo = System.getProperty("foo");

        if(property_foo != null){
            System.out.println(property_foo);
        }
    }
}
