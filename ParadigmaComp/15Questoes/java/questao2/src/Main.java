class Carro {
    String marca;
    String modelo;
    int ano;
    int velocidade = 0;

    Carro(String marca, String modelo, int ano) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
    }

    void acelerar() {
        velocidade += 10;
    }

    void frear() {
        if (velocidade > 0) {
            velocidade -= 10;
        }
    }

    void exibirVelocidade() {
        System.out.println("Velocidade atual: " + velocidade + " km/h");
    }
}

public class Main {
    public static void main(String[] args) {
        Carro carro = new Carro("Ford", "Mustang", 2022);
        carro.acelerar();
        carro.exibirVelocidade();
        carro.frear();
        carro.exibirVelocidade();
    }
}
