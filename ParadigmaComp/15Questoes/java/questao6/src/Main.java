class Motor {
    String tipo;

    Motor(String tipo) {
        this.tipo = tipo;
    }

    String getTipo() {
        return tipo;
    }
}

class Carro {
    String marca;
    Motor motor;

    Carro(String marca, Motor motor) {
        this.marca = marca;
        this.motor = motor;
    }

    void exibirDetalhes() {
        System.out.println("Carro: " + marca + ", Motor: " + motor.getTipo());
    }
}

public class Main {
    public static void main(String[] args) {
        Motor motorV8 = new Motor("V8");
        Carro carro = new Carro("Ford", motorV8);
        carro.exibirDetalhes();
    }
}
