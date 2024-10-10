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
    public static void emitirSomDosAnimais(Animal[] animais) {
        for (Animal animal : animais) {
            animal.som();
        }
    }

    public static void main(String[] args) {
        Animal[] animais = { new Cachorro(), new Gato() };
        emitirSomDosAnimais(animais);
    }
}
