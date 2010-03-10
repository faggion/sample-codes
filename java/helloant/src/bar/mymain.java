package bar;

//import foo.mypkg;
import foo.*;

public class mymain {
    public static void main(String[] args) {
        foo.mypkg pkg = new foo.mypkg();
        pkg.hello();
    }
}
