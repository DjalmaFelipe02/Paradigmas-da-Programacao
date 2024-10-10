class Matematica {
    // Método estático para calcular o fatorial de um número
    public static int fatorial(int numero) {
        if (numero == 0 || numero == 1) {
            return 1;
        } else {
            return numero * fatorial(numero - 1);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        int numero = 5;
        System.out.println("Fatorial de " + numero + ": " + Matematica.fatorial(numero));
    }
}
