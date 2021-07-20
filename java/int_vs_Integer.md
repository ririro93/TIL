# int vs Integer
- int : primitive type
- Integer : Wrapper class 

## Boxing, Unboxing
```java
public class test {
    public static void main(String[] args) {
        int x = 3;
        testing(x);
    }

    public static void testing(Integer a) {
        System.out.println(a.getClass());
    }
}
// -> class java.lang.Integer
```
- automatic process
- boxing : int -> Integer
- unboxing : Integer -> int

```java
public class test {
    public static void main(String[] args) {
        Integer a = 3;
        int b = 3;
        System.out.println(System.identityHashCode(a));
        System.out.println(System.identityHashCode(b));
    }
}

// -> 925858445
// -> 925858445
```

- `identityHashCode(Object x)` : returns hash code for given object
    - if x is int it is automatically boxed into Integer -> thus a, b same value