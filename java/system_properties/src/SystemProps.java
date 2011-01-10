import java.util.Properties;

// HelloWorld.java
public class SystemProps {
    public static void main(String[] args) {
        System.out.println("Hello, Java.");
        Properties prop = System.getProperties();
        System.out.println("classpath = " + prop.getProperty("java.class.path", null));

        String property_foo = System.getProperty("foo");

        if(property_foo != null){
            System.out.println(property_foo);
        }
    }
}
