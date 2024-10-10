class Animal {
    void som() {
        System.out.println("O animal faz um som");
    }
}

class Cachorro extends Animal {
    @Override
    void som() {
        System.out.println("O cachorro late");
    }
}

class Gato extends Animal {
    @Override
    void som() {
        System.out.println("O gato mia");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal cachorro = new Cachorro();
        Animal gato = new Gato();

        cachorro.som();
        gato.som();
    }
}
